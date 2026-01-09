import httpx
from app.core.config import settings

class OllamaClient:
    def __init__(self):
        self.base_url = settings.OLLAMA_BASE_URL
        self.model = settings.MODEL_NAME

    async def generate(self, prompt: str, temperature: float) -> dict:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature
            }
        }
        
        async with httpx.AsyncClient(timeout=settings.TIMEOUT) as client:
            try:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as exc:
                raise ConnectionError(f"Error conectando con Ollama: {exc}")
            except httpx.HTTPStatusError as exc:
                raise ValueError(f"Ollama devolvió un error: {exc.response.text}")