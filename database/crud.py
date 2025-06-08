
from .models import Task, Database

### file hahing methods working on db (using singleton pattern)
### every element of CRUD added

#def add_task_to_db(task: Task):
def add_task_to_db(taskName, taskDate):
    task = Task(name=taskName,date=taskDate)
    session = Database().get_session()
    session.add(task)
    session.commit()
    session.close()

def get_tasks_by_date(date_str: str):
    session = Database().get_session()
    tasks = session.query(Task).filter_by(date=date_str).all()
    session.close()
    return tasks

def update_task_date(task_id: int, new_date: str):
    session = Database().get_session()
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.date = new_date
        session.commit()
    session.close()

def remove_task(task_id: int):
    session = Database().get_session()
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
    session.close()

def set_task_progress(task_id, value):
    session = Database().get_session()
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.progress = value
        task.completed = (value == 100)
        session.commit()
    session.close()

def get_task_by_id(task_id):
    session = Database().get_session()
    task = session.query(Task).filter_by(id=task_id).first()
    session.close()
    return task