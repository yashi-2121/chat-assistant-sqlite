from flask import Flask, request, jsonify
import sqlite3
import re

app = Flask(__name__)

def execute_query(query, params=()):
    """Executes an SQL query and returns the results."""
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

def process_query(user_input):
    """Processes user input and returns an appropriate response."""
    user_input = user_input.lower()

    # Query 1: Show all employees in a department
    match = re.match(r"show me all employees in the (.+) department", user_input)
    if match:
        department = match.group(1).capitalize()
        employees = execute_query("SELECT Name FROM Employees WHERE Department = ?", (department,))
        return ", ".join([emp[0] for emp in employees]) if employees else f"No employees found in {department} department."

    # Query 2: Who is the manager of a department?
    match = re.match(r"who is the manager of the (.+) department", user_input)
    if match:
        department = match.group(1).capitalize()
        manager = execute_query("SELECT Manager FROM Departments WHERE Name = ?", (department,))
        return f"The manager of {department} department is {manager[0][0]}." if manager else f"No manager found for {department}."

    # Query 3: Employees hired after a certain date
    match = re.match(r"list all employees hired after (\d{4}-\d{2}-\d{2})", user_input)
    if match:
        hire_date = match.group(1)
        employees = execute_query("SELECT Name FROM Employees WHERE Hire_Date > ?", (hire_date,))
        return ", ".join([emp[0] for emp in employees]) if employees else f"No employees hired after {hire_date}."

    return "Sorry, I didn't understand your query."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("query")
    if not user_input:
        return jsonify({"response": "Please provide a query."})
    
    response = process_query(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
