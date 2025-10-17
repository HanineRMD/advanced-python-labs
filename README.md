 🧠 Advanced Python Labs – FastAPI, Streamlit & API Testing

This repository contains all lab assignments for the **Advanced Python** course , focused on building web APIs, testing endpoints, and deploying interactive applications.

---

## 📁 Repository Structureadvanced-python-labs/
advanced-python-labs/
├── lab1_fastapi/
│   ├── main.py
│   ├── README.md
├── screenshots/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
├── README.md  ← global README for the whole repo


## 🚀 Lab 1 – FastAPI

### 🎯 Objective
Build a RESTful API using FastAPI to manage a to-do list with full CRUD operations.

### ⚙️ How to Run
cd lab1_fastapi
uvicorn main:app --reload

📌 Endpoints Overview
| Method | Endpoint            | Description         |
|--------|---------------------|---------------------|
| GET    | `/`                 | Welcome message     |
| POST   | `/items`            | Add a new item      |
| GET    | `/items?limit=N`    | List first N items  |
| PUT    | `/items/{item_id}`  | Update item by ID   |
| DELETE | `/items/{item_id}`  | Delete item by ID   |


## 🖼️ Screenshots

| File Name | Description | 📸 Preview|
|-----------|-------------|-------------|
| `1.png`   | FastAPI running with "Hello World!" |![Hello World](screenshots/1.png)  |
| `2.png`   | Add a new item (e.g. `{"id":1,"name":"apple"}`) |![Add Item](screenshots/2.png) |
| `3.png`   | GET `/items` showing all items |![List Items](screenshots/3.png)  |
| `4.png`   | PUT `/items/1` to update item |![Update Item](screenshots/4.png)  |
| `5.png`   | DELETE `/items/1` to remove item |![Delete Item](screenshots/5.png)|




🛠️ Technologies Used
-  Python 3.11+ – Core programming language
-  FastAPI – High-performance web framework
-  Uvicorn – ASGI server for FastAPI
-  Pydantic – Data validation and parsing
-  Postman – API testing and debugging
-  Git – Version control
-  GitHub / 🦊 GitLab – Code hosting platform


👩‍💻 Author
Hanine Ramdhane
GitHub: @HanineRMD
GitLab: @hanineramdhane

