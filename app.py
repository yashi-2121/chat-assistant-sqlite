import os
from flask import Flask, request, jsonify
import sqlite3
import re
from datetime import datetime
from flask import render_template

app = Flask(__name__)

def execute_query(query, params=()):
    connection = sqlite3.connect('chat_assistant.db')
    cursor = connection.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    connection.close()
    return results

def extract_department(query):
    match = re.search(r"in the (\w+) department", query, re.IGNORECASE)
    return match.group(1) if match else None

def extract_date(query):
    match = re.search(r"after (\d{4}-\d{2}-\d{2})", query)
    return match.group(1) if match else None

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

@app.route('/')
def home():
    return "Welcome to the Chat Assistant!"

@app.route('/chat', methods=['POST'])
def chat():
    query = request.json.get('query')
    
    if not query:
        return jsonify({"response": "No query provided."})

    if "Show me all employees in the" in query:
        department = extract_department(query)
        if not department:
            return jsonify({"response": "Please specify a valid department name."})
        
        sql_query = "SELECT Name FROM Employees WHERE Department = ?"
        result = execute_query(sql_query, (department,))
        
        if result:
            return jsonify({"response": f"Employees in {department}: {', '.join([row[0] for row in result])}."})
        else:
            return jsonify({"response": f"No employees found in {department}."})

    elif "Who is the manager of the" in query:
        department = extract_department(query)
        if not department:
            return jsonify({"response": "Please specify a valid department name."})

        sql_query = "SELECT Manager FROM Departments WHERE Name = ?"
        result = execute_query(sql_query, (department,))
        
        if result:
            return jsonify({"response": f"The manager of {department} is {result[0][0]}."})
        else:
            return jsonify({"response": "No department found with this name."})

    elif "List all employees hired after" in query:
        date = extract_date(query)
        if not date or not is_valid_date(date):
            return jsonify({"response": "Invalid date format. Please use YYYY-MM-DD."})

        sql_query = "SELECT Name FROM Employees WHERE Hire_Date > ?"
        result = execute_query(sql_query, (date,))
        
        if result:
            return jsonify({"response": f"Employees hired after {date}: {', '.join([row[0] for row in result])}."})
        else:
            return jsonify({"response": "No employees hired after this date."})

    elif "Show the highest-paid employee" in query:
        sql_query = "SELECT Name, Salary, Department FROM Employees ORDER BY Salary DESC LIMIT 1"
        result = execute_query(sql_query)
        
        if result:
            name, salary, department = result[0]
            return jsonify({"response": f"The highest-paid employee is {name} from {department} with a salary of ${salary}."})
        else:
            return jsonify({"response": "No employee data available."})

    elif "What is the total salary expense for the" in query:
        department = extract_department(query)
        if not department:
            return jsonify({"response": "Please specify a valid department name."})

        sql_query = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
        result = execute_query(sql_query, (department,))
        
        if result and result[0][0]:
            return jsonify({"response": f"The total salary expense for {department} is ${result[0][0]}."})
        else:
            return jsonify({"response": f"No salary data found for the {department} department."})
    
    else:
        return jsonify({"response": "Sorry, I couldn't understand the query. Please try again."})

@app.route('/ui')
def chat_ui():
    return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Default to 10000 if no env variable
    app.run(host="0.0.0.0", port=port, debug=True)
    
