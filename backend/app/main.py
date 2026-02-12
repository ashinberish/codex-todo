from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def healthcheck():
    return {"status": "ok"}


@app.get("/todos", response_model=list[schemas.Todo])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)


@app.post("/todos", response_model=schemas.Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)


@app.put("/todos/{todo_id}", response_model=schemas.Todo)
def update_todo(
    todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)
):
    todo_model = crud.get_todo(db, todo_id)
    if not todo_model:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud.update_todo(db, todo_model, todo)


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = crud.get_todo(db, todo_id)
    if not todo_model:
        raise HTTPException(status_code=404, detail="Todo not found")
    crud.delete_todo(db, todo_model)
    return None
