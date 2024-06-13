from fastapi import APIRouter
from app.schemas.team import TeamSchema, TeamResponseSchema
from app.models.team import Team

router = APIRouter()

@router.post("/teams")
async def create_team(team: TeamSchema):
    new_team = Team(name=team.name)
    session.add(new_team)
    session.commit()
    return {"message": "Team created successfully"}

@router.get("/teams")
async def get_teams():
    teams = session.query(Team).all()
    return [{"id": team.id, "name": team.name, "created_at": team.created_at} for team in teams]