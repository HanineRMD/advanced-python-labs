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

|  GET| / | Welcome message | 
|  POST | /items | Add a new item | 
|  GET| /items?limit=N | Retrieve item by ID | 
|  PUT| /items/{item_id} | Update item by ID | 
|  DELETE| /items/{item_id} | Delete item by ID | 



🖼️ Screenshots (CAPs)
|  |  | 
| Capture d'écran 2025-10-10 190624.png | FastAPI running in browser with {"Hello":"World"} | 
| Capture d'écran 2025-10-10 190815.png | Add a new item | 
| Capture d'écran 2025-10-10 190946.png | GET /items?limit=3 Successful with multiple items| 
| Capture d'écran 2025-10-10 191741.png | Successful to update item | 
| Capture d'écran 2025-10-10 191807.png | Successful to remove item | 


🛠️ Technologies Used
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


