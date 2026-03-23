from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse


router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest) -> ChatResponse:
    return ChatResponse(
        reply=f"收到你的消息：{payload.message}",
        session_id=payload.session_id,
        status="ok",
    )
