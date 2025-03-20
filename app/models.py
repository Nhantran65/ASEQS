from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    message_type = Column(String, index=True)
    content = Column(Text, nullable=False)
    response = Column(Text, nullable=True)
