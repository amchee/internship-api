# Internship API

This project is a RESTful API built with Flask, SQLAlchemy, and Flask-RESTful to manage users, universities, and interns in an internship system.

## 👨‍💻 Developed by

**Amel Adzemi**

---

## 🚀 Features

* User registration and login with JWT authentication
* CRUD operations for Interns and Universities
* Relational data: interns are linked to universities
* Token-protected endpoints for modifying data
* SQLite as a development database
* Includes unit, integration, and system tests

---

## 🛠 Technologies Used

* Python 3
* Flask
* Flask-RESTful
* Flask-JWT-Extended
* SQLAlchemy
* Postman (for API testing)
* Unittest (for Python testing)

---

## 📁 Project Structure

```
intership-api/
├── main.py
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── models/
│   │   ├── user.py
│   │   ├── intern.py
│   │   └── university.py
│   └── resources/
│       ├── user.py
│       ├── intern.py
│       └── university.py
├── tests/
│   ├── unit/
│   │   └── test_unit.py
│   ├── integration/
│   │   └── test_integration.py
│   └── system/
│       └── test_system.py
└── Postman/
    ├── internship_api_collection.json
    └── internship_api_environment.json
```

---

## 🔐 Authentication

* Register at `/register`
* Login at `/login`
* Use `Bearer <token>` in the `Authorization` header for protected routes

---

## 🧪 Testing

### ✅ Unit Tests

Location: `tests/unit/test_unit.py`

* Tests individual models: `UserModel`, `UniversityModel`, `InternModel`

### 🔗 Integration Tests

Location: `tests/integration/test_integration.py`

* Verifies interaction between intern and university models

### 🌐 System Tests

Location: `tests/system/test_system.py`

* Simulates full workflow:

  * Register user
  * Login
  * Create university
  * Create intern

To run all tests:

```bash
python -m unittest discover
```

---

## 🧪 Postman Testing

* Collection and environment JSON files included
* Tests cover:

  * User registration & login
  * University creation & listing
  * Intern creation, listing, updating, deleting

Use Postman's Collection Runner for system-level API testing.

---

## 📌 Final Notes

* Database is SQLite and resets if `data.db` is deleted
* All protected endpoints require a valid JWT
* A `description` field was added to the Intern model as a custom extension

---

Thank you for reviewing this project!
Feel free to reach out if you have questions or suggestions.

— Amel Adzemi
