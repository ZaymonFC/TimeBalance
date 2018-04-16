from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Activity(Base):
    __tablename__ = "activites"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    target = Column(Integer)

class Task(Base):
    id = Column(Integer, primary_key=True)
    time = Column(DateTime, default=datetime.datetime.utcnow)
    duration = Column(Integer)
    activity_id = Column(Integer, ForeignKey(activities.id))

    activity = relationship("Activity", back_populates="tasks")
