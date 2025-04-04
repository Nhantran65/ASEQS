from pydantic import BaseModel
from datetime import datetime

class MessageBase(BaseModel):
    message_type: str
    content: str

class MessageCreate(MessageBase):
    pass

class MessageResponse(MessageBase):
    id: int
    response: str | None = None
    created_at: datetime

    class Config:
        orm_mode = True


class CodeAnalysisRequest(BaseModel):
    filename: str
    source_code: str
    sonar_output: str
    codescene_output: str

class CodeAnalysisResponse(BaseModel):
    llm_feedback: str