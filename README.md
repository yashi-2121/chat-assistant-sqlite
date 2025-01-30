# Chat Assistant for SQLite Database

## 🚀 Overview
This is a simple chat assistant that interacts with an SQLite database to answer user queries. It is built using Flask and supports various queries related to employees and departments.

## 🏗 Features
- Accepts natural language queries.
- Converts queries into SQL to fetch data from an SQLite database.
- Returns structured responses in JSON format.
- Handles errors gracefully.

## 🗂 Database Schema
This project uses an SQLite database with the following tables:

### Employees Table:
| ID | Name   | Department  | Salary | Hire_Date  |
|----|--------|------------|--------|------------|
| 1  | Alice  | Sales      | 50000  | 2021-01-15 |
| 2  | Bob    | Engineering| 70000  | 2020-06-10 |
| 3  | Charlie| Marketing  | 60000  | 2022-03-20 |

### Departments Table:
| ID | Name         | Manager |
|----|-------------|---------|
| 1  | Sales       | Alice   |
| 2  | Engineering | Bob     |
| 3  | Marketing   | Charlie |

## 🛠 Supported Queries
- "Show me all employees in the [department] department."
- "Who is the manager of the [department] department?"
- "List all employees hired after [date]."
- "What is the total salary expense for the [department] department?"

## 📦 Installation & Setup
### 1️⃣ Clone the Repository:
```sh
 git clone https://github.com/yashi-2121/chat-assistant-sqlite.git
 cd chat-assistant-sqlite
```

### 2️⃣ Install Dependencies:
```sh
 pip install -r requirements.txt
```

### 3️⃣ Initialize the Database:
```sh
 python init_db.py
```

### 4️⃣ Run the Flask Application:
```sh
 python app.py
```


## 🔒 Security Improvements
- Use **parameterized queries** to prevent SQL injection.
- Implement **input validation** to handle incorrect department names and invalid dates.

## 🏗 Code Quality Improvements
- Refactor `app.py` to make it more modular by separating database queries into a separate helper function.
- Improve error handling for unexpected inputs.
- Add comments and docstrings to improve readability.

## 🎨 User Experience Enhancements
- Provide clearer error messages.
- Add a simple front-end UI for a better chat experience.
- Implement logging to track API usage and errors.

## 🧪 Testing
- Add unit tests for database queries and API responses using `pytest`.
- Ensure the assistant correctly handles invalid inputs and edge cases.

## 🚀 Deployment
This project is deployed on Render. You can access it at:
```
 https://chat-assistant-sqlite.onrender.com/ui
```

## 📜 Known Limitations & Future Improvements
- Currently, it supports only a predefined set of queries.
- Can be extended to support more complex natural language processing.
- Add authentication for secure access.

---
Made with ❤️ by Yashi Naik

