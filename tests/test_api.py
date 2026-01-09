import pytest
from httpx import AsyncClient
from app.main import app
from app.core.config import settings
from app.services.llm_service import LLMService
from app.models.schemas import ChatResponse

# Mock Service
class MockLLMService:
    async def get_response(self, prompt: str, temperature: float) -> ChatResponse:
        return ChatResponse(
            response=f"Mocked response for: {prompt}",
            model="mock-model",
            done=True
        )

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": settings.PROJECT_NAME}

@pytest.mark.asyncio
async def test_chat_endpoint_valid_key():

    app.dependency_overrides[LLMService] = lambda: MockLLMService() 

    
    from app.api.v1.chat_router import get_llm_service
    app.dependency_overrides[get_llm_service] = lambda: MockLLMService()

    headers = {"X-API-Key": settings.API_KEY}
    payload = {"prompt": "Hello", "temperature": 0.5}
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(f"{settings.API_V1_STR}/chat", json=payload, headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["response"] == "Mocked response for: Hello"
    assert data["model"] == "mock-model"
    
    # Clean up
    app.dependency_overrides = {}

@pytest.mark.asyncio
async def test_chat_endpoint_invalid_key():
    headers = {"X-API-Key": "wrong-key"}
    payload = {"prompt": "Hello"}
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(f"{settings.API_V1_STR}/chat", json=payload, headers=headers)
    
    assert response.status_code == 403
