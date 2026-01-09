from app.services.clients.ollama_client import OllamaClient
from app.models.schemas import ChatResponse

class LLMService:
    def __init__(self, client: OllamaClient = None):
        self.client = client or OllamaClient()

    async def get_response(self, prompt: str, temperature: float) -> ChatResponse:

        prompt_final = f"Eres un doctor experto. {prompt}"
        
        raw_response = await self.client.generate(prompt, temperature)
        
        return ChatResponse(
            response=raw_response.get("response", ""),
            model=raw_response.get("model", "unknown"),
            done=raw_response.get("done", False)
        )