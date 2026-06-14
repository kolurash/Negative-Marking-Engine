# 🚀 Negative Marking Engine

A simple and efficient backend API built using **FastAPI** to calculate exam scores with a negative marking system.

## 📌 Project Overview

The Negative Marking Engine accepts the number of correct and wrong answers, applies the negative marking formula, and returns the final score as a JSON response.

This project demonstrates:
- REST API development with FastAPI
- Request validation using Pydantic
- Error handling with HTTP exceptions
- Automated testing using Pytest

---

## 🎯 Features

- ✅ Calculate final score using negative marking
- ✅ Input validation
- ✅ Handles missing required fields
- ✅ Prevents negative input values
- ✅ Returns JSON responses
- ✅ Interactive API documentation with Swagger UI
- ✅ Unit tests using Pytest

---

## 🛠️ Tech Stack

- Python 3
- FastAPI
- Uvicorn
- Pydantic
- Pytest

---

## 📂 Project Structure

```
Negative-Marking-Engine/
│
├── app.py
├── requirements.txt
├── README.md
├── tests/
│   └── test_app.py
└── .venv/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/kolurash/Negative-Marking-Engine.git
```

### Move into the project directory

```bash
cd Negative-Marking-Engine
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The server will run at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📥 API Endpoint

### POST `/calculate-score`

### Request

```json
{
  "correct": 8,
  "wrong": 2
}
```

### Formula

```
Final Score = Correct Answers - (Wrong Answers × 0.25)
```

### Response

```json
{
  "final_score": 7.5
}
```

---

## ❌ Invalid Input Example

### Request

```json
{
  "correct": -1,
  "wrong": 2
}
```

### Response

```json
{
  "detail": "Values cannot be negative"
}
```

---

## 🧪 Running Tests

Run all tests using:

```bash
pytest
```

Example output:

```text
=============================
3 passed in 0.xx seconds
=============================
```

---

## 📖 Example Calculation

Input:

```json
{
  "correct": 10,
  "wrong": 4
}
```

Calculation:

```
10 - (4 × 0.25)
= 10 - 1
= 9
```

Output:

```json
{
  "final_score": 9.0
}
```

---

## 🎯 Future Enhancements

- Support configurable negative marking values
- Support multiple subjects
- Store exam history in a database
- User authentication
- Leaderboard and analytics
- Docker deployment

---
