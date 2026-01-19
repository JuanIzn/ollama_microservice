# ⚙️ Ollama MicroService

A high-performance, containerized API gateway built with **FastAPI** that wraps the **Ollama** engine. This service provides a structured, secure, and production-ready interface for interacting with Large Language Models (LLMs) like Llama 3.

## 🔑 Key Features

- **FastAPI Framework**: High performance, and automatically generated OpenAPI documentation.
- **Ollama Integration**: Seamless connection to the Ollama engine for local LLM execution.
- **Security**: Simple yet effective API Key authentication via headers.
- **Dockerized Architecture**: Fully containerized using Docker and Docker Compose, including NVIDIA GPU support.
- **Health Monitoring**: Built-in health check endpoint for service status verification.
- **Strict Validation**: Pydantic models for request and response data integrity.

## 🏗️ Architecture

The system consists of two main components orchestrated by Docker Compose:

1.  **FastAPI Gateway (`fastapi-app`)**: Handles incoming HTTP requests, performs authentication, validates payloads, and communicates with the Ollama backend.
2.  **Ollama Engine (`ollama-engine`)**: A dedicated service that manages and executes LLM models (e.g., Llama 3). It is configured to utilize NVIDIA GPUs for accelerated inference.

---

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) (if needed)

### ⚙️ Configuration

Create a `.env` file in the root directory with the following the .env.example variables.

### Deployment

1.  **Build and start the containers:**
    ```bash
    docker-compose up -d --build
    ```
    *Note: The first run will automatically pull the `llama3` model.*

2.  **Verify the services are running:**
    ```bash
    docker-compose ps
    ```

3.  **Check logs (optional):**
    ```bash
    docker-compose logs -f
    ```

## 🧪 Testing

### Health Check
Verify the gateway is up and running:
```bash
curl http://localhost:8000/health
```

### Chat Endpoint
Send a prompt to the LLM. Replace `your_secure_api_key_here` with the key defined in your `.env`:

```bash
curl -X POST http://localhost:8000/api/v1/chat \
     -H "Content-Type: application/json" \
     -H "X-API-Key: your_secure_api_key_here" \
     -d '{
           "prompt": "I have pain in my leg.", #the "health issue" here
           "temperature": 0.7
         }'
```

## 🚥 API Documentation

Once the service is running, you can access the interactive Swagger UI at:
- [http://localhost:8000/docs](http://localhost:8000/docs)


