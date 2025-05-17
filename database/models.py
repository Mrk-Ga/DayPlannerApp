from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from screens.TaskGUI import TaskBox

Base = declarative_base()
'''
if platform == 'android':
    from android.storage import app_storage_path
    db_path = os.path.join(app_storage_path(), 'planer.db')
else:
    db_path = 'planer.db'


'''

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
    #day_id = Column(Integer, ForeignKey('days.id'))
    #day = relationship('Day', back_populates='tasks')

    def __repr__(self):
        return f"<Task(name='{self.name}', day='{self.date}', completed={self.completed})>"

def add_task_to_db(task: Task):
    session.add(task)
    session.commit()

def read_tasks_from_db_by_date(parent_screen, date):
    for task in get_tasks_by_date(date):
        parent_screen.ids.task_list.add_widget(
            TaskBox(text=task.name)
        )

def get_tasks_by_date(date_str: str):
    tasks = session.query(Task).filter_by(date=date_str).all()
    return tasks

engine = create_engine('sqlite:///planer.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


