from fastapi import APIRouter
from app.schemas.agent import AgentRequest, AgentResponse
from app.agent.runtime import run_agent

from app.schemas.chat import ChatRequest


router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=AgentResponse)
async def chat(payload: ChatRequest) -> AgentResponse:
    agent_request = AgentRequest(
        message=payload.message,
        session_id=payload.session_id,
        history=[]
    )
    return run_agent(agent_request)
