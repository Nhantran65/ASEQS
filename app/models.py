from sqlalchemy import Column, Integer, String, Text, DateTime, func
from .database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    message_type = Column(String(50), index=True)
    content = Column(Text, nullable=False)
    response = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    source_code = Column(Text)
    sonar_output = Column(Text)
    codescene_output = Column(Text)
    llm_feedback = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)