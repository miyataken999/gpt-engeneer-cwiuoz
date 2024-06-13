from pydantic import BaseModel

class TeamSchema(BaseModel):
    name: str

class TeamResponseSchema(BaseModel):
    id: int
    name: str
    created_at: datetime