"""Web UI for Dinesh Assistant using FastAPI."""

import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from src.chatbot import DineshAssistant

# Initialize FastAPI app with additional configuration
app = FastAPI(
    title="Dinesh Assistant",
    description="ChatBot for Python & Github project - Your AI-powered project assistant",
    version="1.0.0",
    docs_url="/docs",  # Enable Swagger UI
    redoc_url="/redoc",  # Enable ReDoc
)

# Set up static files and templates
web_dir = Path(__file__).parent
static_dir = web_dir / "static"
templates_dir = web_dir / "templates"


# Add startup and shutdown events
@app.on_event("startup")
async def startup_event():
    """Initialize resources on startup."""
    print("🚀 Server starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    """Clean up resources on shutdown."""
    print("🔄 Server shutting down...")


app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
templates = Jinja2Templates(directory=str(templates_dir))

# Initialize chatbot
assistant = DineshAssistant()


class ChatRequest(BaseModel):
    """Chat request model."""

    query: str


class ChatResponse(BaseModel):
    """Chat response model."""

    text: str
    confidence: float
    references: List[str]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    """Serve the chat interface."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/greet")
async def greet() -> Dict:
    """Get initial greeting."""
    return {
        "text": "Hello! 👋 I'm your project assistant. Ask me about:\n"
        "• Project features and capabilities\n"
        "• Implementation details\n"
        "• Documentation and guides",
        "confidence": 1.0,
        "references": [],
    }


@app.get("/health")
async def health_check() -> Dict:
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "uptime": "available",
    }


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> Dict:
    """Handle chat messages."""
    try:
        query = request.query.lower().strip()
        print(f"Processing query: {query}")  # Debug log

        # Get response from assistant for all queries
        print("Using assistant for response")  # Debug log
        response = await assistant.respond(request.query)

        print(f"Response received: {response.text[:100]}...")  # Debug log
        return {
            "text": response.text,
            "confidence": response.confidence,
            "references": response.references,
        }

    except Exception as e:
        logging.error(f"Chat error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle all uncaught exceptions."""
    logging.error(f"Uncaught exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred. Please try again later."},
    )


def start() -> None:
    """Start the web UI server with robust configuration for permanent access."""
    import socket
    import time

    import uvicorn

    def find_free_port(start_port: int = 8000) -> int:
        """Find a free port starting from the given port."""
        port = start_port
        max_attempts = 100

        for _ in range(max_attempts):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind(("127.0.0.1", port))
                    s.close()
                    time.sleep(0.1)  # Give OS time to fully release the port
                    return port
            except OSError:
                port += 1

        raise RuntimeError(
            "Could not find a free port after {} attempts".format(max_attempts)
        )

    port = find_free_port(8000)
    print(f"\n🤖 Dinesh Assistant is now running!")
    print(f"🌐 Access the web interface at: http://localhost:{port}")
    print("⌨️  Press Ctrl+C to stop the server when needed\n")

    uvicorn.run(app, host="127.0.0.1", port=port, log_level="debug", reload=True)
