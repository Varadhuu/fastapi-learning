from fastapi import APIRouter, HTTPException
from ..models.chat import ChatRequest, ChatResponse
from ..services.groq_services import generate_response

router = APIRouter(prefix="/chat", tags=["Chatbot"])

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(chat_request: ChatRequest):
    try:
        reply = await generate_response(chat_request.user_message)
        return ChatResponse(response=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))