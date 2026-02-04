from sqlalchemy.orm import Session

from . import models, schemas


def get_todos(db: Session) -> list[models.Todo]:
    return db.query(models.Todo).order_by(models.Todo.id.desc()).all()


def get_todo(db: Session, todo_id: int) -> models.Todo | None:
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def create_todo(db: Session, todo: schemas.TodoCreate) -> models.Todo:
    todo_model = models.Todo(**todo.model_dump())
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model


def update_todo(
    db: Session, todo_model: models.Todo, todo_update: schemas.TodoUpdate
) -> models.Todo:
    updates = todo_update.model_dump(exclude_unset=True)
    for key, value in updates.items():
        setattr(todo_model, key, value)
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model


def delete_todo(db: Session, todo_model: models.Todo) -> None:
    db.delete(todo_model)
    db.commit()
