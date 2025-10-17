 🧠 Advanced Python Labs – FastAPI, Streamlit & API Testing

This repository contains all lab assignments for the **Advanced Python** course , focused on building web APIs, testing endpoints, and deploying interactive applications.

---

## 📁 Repository Structureadvanced-python-labs/
advanced-python-labs/
├── lab1_fastapi/
├── Pydantic
├── quiz-fastapi
├── screenshots/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
├── README.md  ← global README for the whole repo
├── Requests
├──.gitignore
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

🗄️ TP Quiz – FastAPI & PostgreSQL
🎯 Objectif

Créer une API REST pour gérer un quiz avec questions et choix, persistant dans PostgreSQL.

⚙️ Configuration PostgreSQL
Créer la base de données :
CREATE DATABASE quizapp;

Créer l’utilisateur :
CREATE USER quizuser WITH PASSWORD 'votre_mot_de_passe';

Donner tous les privilèges sur la base :
GRANT ALL PRIVILEGES ON DATABASE quizapp TO quizuser;

Donner les droits sur le schéma public :
GRANT ALL ON SCHEMA public TO quizuser;


⚠️ Le schéma public appartient par défaut au superutilisateur PostgreSQL. Si quizuser n’a pas les droits, il ne pourra pas créer de tables.

⚡ Connexion dans FastAPI

Dans database.py :
DATABASE_URL = "postgresql://quizuser:votre_mot_de_passe@localhost/quizapp"

⚙️ Lancer le projet
cd quiz-fastapi
uvicorn main:app --reload

📌 Endpoints Quiz

|Méthode	Endpoint | Description | 📸 Preview|
|-----------|-------------|-------------|
|POST	/questions/ | 	Créer une question avec choix |![Hello World](screenshots/6.png)  |
|GET	/questions/ | {question_id}	Lire une question |![Add Item](screenshots/7.png) |
|GET	/choices/| {question_id}	Lire les choix d’une question |![List Items](screenshots/8.png |
|GET	/questions-with-choices/{question_id} | Question + choix en une requête|![Update Item](screenshots/9.png)  |


🛠️ Technologies Used
Python 3.11+ – Langage principal

FastAPI – Framework web performant

Uvicorn – ASGI server

Pydantic – Validation et parsing de données

PostgreSQL – Base de données relationnelle

Postman – Test d’API

Git – Gestion de versions

GitHub / GitLab – Hébergement de code


👩‍💻 Author
Hanine Ramdhane
GitHub: @HanineRMD
GitLab: @hanineramdhane

