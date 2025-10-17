# main.py
from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal
import schemas

app = FastAPI(title="Quiz API")

# Crée les tables si elles n'existent pas
models.Base.metadata.create_all(bind=engine)

# Dependency pour obtenir une session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/questions/", status_code=201)
def create_questions(question: schemas.QuestionBase, db: db_dependency):
    db_question = models.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    for choice in question.choices:
        db_choice = models.Choices(
            choice_text=choice.choice_text,
            is_correct=choice.is_correct,
            question_id=db_question.id
        )
        db.add(db_choice)
    db.commit()
    return {"id": db_question.id, "message": "Question créée"}

@app.get("/questions/{question_id}", response_model=schemas.QuestionOut)
def read_questions(question_id: int, db: db_dependency):
    result = db.query(models.Questions).filter(models.Questions.id == question_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Question non trouvée")
    return result

@app.get("/choices/{question_id}", response_model=List[schemas.ChoiceOut])
def read_choices(question_id: int, db: db_dependency):
    result = db.query(models.Choices).filter(models.Choices.question_id == question_id).all()
    if not result:
        raise HTTPException(status_code=404, detail="Choices non trouvées")
    return result

# Optional : endpoint qui retourne question + choix d'un coup
from fastapi.responses import JSONResponse
@app.get("/questions-with-choices/{question_id}")
def question_with_choices(question_id: int, db: db_dependency):
    q = db.query(models.Questions).filter(models.Questions.id == question_id).first()
    if not q:
        raise HTTPException(status_code=404, detail="Question non trouvée")
    choices = db.query(models.Choices).filter(models.Choices.question_id == question_id).all()
    return {"id": q.id, "question_text": q.question_text, "choices": [
        {"id": c.id, "choice_text": c.choice_text, "is_correct": c.is_correct} for c in choices
    ]}
