from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    prompt: str = Field(..., min_length=1, example="Explica la relatividad")
    temperature: float = Field(0.7, ge=0.0, le=1.0)

class ChatResponse(BaseModel):
    response: str
    model: str
    done: bool