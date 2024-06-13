from fastapi import APIRouter, HTTPException
from app.schemas.user import UserSchema, UserResponseSchema
from app.models.user import User

router = APIRouter()

@router.post("/register")
async def register_user(user: UserSchema):
    existing_user = session.query(User).filter_by(username=user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = User(username=user.username, password=user.password, profile=user.profile, team_id=user.team_id, tags=user.tags)
    session.add(new_user)
    session.commit()
    return {"message": "User created successfully"}

@router.post("/login")
async def login_user(username: str, password: str):
    user = session.query(User).filter_by(username=username, password=password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Logged in successfully"}

@router.get("/users")
async def get_users():
    users = session.query(User).all()
    return [{"id": user.id, "username": user.username, "profile": user.profile} for user in users]

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "username": user.username, "profile": user.profile, "tags": user.tags}