# 🧠 Advanced Python Labs – FastAPI, Streamlit & API Testing

This repository contains all lab assignments for the **Advanced Python** course , focused on building web APIs, testing endpoints, and deploying interactive applications.

---

## 📁 Repository Structure
advanced-python-labs/ ├── lab1_fastapi/ │   ├── main.py │   ├── README.md ├── lab2_streamlit/ │   ├── app.py │   ├── README.md ├── screenshots/ │  
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



🖼️ Screenshots (CAPs)

| screenshots/1.png | FastAPI running in browser with {"Hello":"World"} | 
| screenshots/2.png | Add a new item | 
| screenshots/3.png | GET /items?limit=3 Successful with multiple items| 
| screenshots/4.png | Successful to update item | 
| screenshots/5.png | Successful to remove item | 

### 🛠️ Technologies Used
- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic
- Postman
- Git & GitHub / GitLab


👩‍💻 Author
Hanine Ramdhane
GitHub: @HanineRMD
GitLab: @hanineramdhane


