from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from app.core.config import settings
from app.models.schemas import ChatRequest, ChatResponse
from app.services.llm_service import LLMService

router = APIRouter()
api_key_header = APIKeyHeader(name="X-API-Key")

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Credenciales inválidas")
    return api_key

def get_llm_service() -> LLMService:
    return LLMService()

@router.post("/chat", response_model=ChatResponse, dependencies=[Depends(verify_api_key)])
async def chat(request: ChatRequest, service: LLMService = Depends(get_llm_service)):
    try:
        return await service.get_response(request.prompt, request.temperature)
    except ConnectionError:
        raise HTTPException(status_code=503, detail="El servicio de IA no está disponible.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))