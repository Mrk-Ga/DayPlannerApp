import os

from kivy.utils import platform
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

if platform == 'android':
    from android.storage import app_storage_path
    db_path = os.path.join(app_storage_path(), 'planer.db')
else:
    db_path = 'planer.db'





class Day(Base):
    __tablename__ = 'days'

    id = Column(Integer, primary_key=True)
    date = Column(String, unique=True)  # np. "2025-05-17"

    #tasks = relationship('Task', back_populates='day', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Day(date='{self.date}', tasks={len(self.tasks)})>"

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    progress = Column(Integer, default=0)  # 0–100
    completed = Column(Boolean, default=False)
    date = Column(String)

    def __repr__(self):
        return f"<Task(name='{self.name}', day='{self.date}', completed={self.completed})>"

def add_task_to_db(task: Task):
    session.add(task)
    session.commit()




def get_tasks_by_date(date_str: str):

    tasks = session.query(Task).filter_by(date=date_str).all()
    return tasks

def update_task_date(task_id: int, new_date: str):
    task = session.query(Task).filter_by(id=task_id).first()

    if task:
        # Zmień datę
        task.date = new_date

        # Zatwierdź zmiany
        session.commit()
        print(f"Zaktualizowano datę zadania (id={task_id}) na {new_date}")
    else:
        print(f"Nie znaleziono zadania o id={task_id}")

def remove_task(task_id: int):
    # Pobierz zadanie o danym id
    task = session.query(Task).filter_by(id=task_id).first()

    if task:
        # Usuń zadanie z sesji
        session.delete(task)
        # Zatwierdź zmiany
        session.commit()
        print(f"Usunięto zadanie o id={task_id}")
    else:
        print(f"Nie znaleziono zadania o id={task_id}")

def set_task_progress(taskID, value):
    task = session.query(Task).filter_by(id=taskID).first()
    task.progress = value
    session.commit()

def set_task_if_completed(taskID, completed):
    task = session.query(Task).filter_by(id=taskID).first()
    task.completed = completed
    session.commit()



engine = create_engine(f'sqlite:///{db_path}')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


