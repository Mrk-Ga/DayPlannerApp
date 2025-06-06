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

###SIGLETON FOR DB ACCESS
class Database:
    _instance = None

    def __new__(cls, db_path=db_path):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._init_db(db_path)
        return cls._instance

    def _init_db(self, path):
        self.engine = create_engine(f'sqlite:///{path}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

### main table in database, used to store tasks informations
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


