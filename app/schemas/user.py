from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str
    profile: str
    team_id: int
    tags: str

class UserResponseSchema(BaseModel):
    id: int
    username: str
    profile: str
    team_id: int
    tags: str