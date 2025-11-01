"""Web UI for Dinesh Assistant using FastAPI."""

from pathlib import Path
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from ..chatbot import DineshAssistant

# Initialize FastAPI app
app = FastAPI(title="Dinesh Assistant")

# Set up static files and templates
web_dir = Path(__file__).parent
static_dir = web_dir / "static"
templates_dir = web_dir / "templates"

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
    return {"text": assistant.greet(), "confidence": 1.0, "references": []}


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> Dict:
    """Handle chat messages."""
    try:
        # Get response from assistant
        response = await assistant.respond(request.query)

        return {
            "text": response.text,
            "confidence": response.confidence,
            "references": response.references,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")


def start() -> None:
    """Start the web UI server with graceful shutdown."""
    import signal
    import sys

    import uvicorn

    def handle_exit(signum, frame):
        print("\nReceived signal to terminate. Shutting down gracefully...")
        sys.exit(0)

    # Register signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, handle_exit)  # Handles Ctrl+C
    signal.signal(signal.SIGTERM, handle_exit)  # Handles termination request

    config = uvicorn.Config(
        "src.web.app:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        reload_delay=1.0,
        log_level="info",
        access_log=True,
        workers=1,
    )

    server = uvicorn.Server(config)
    print("\n🤖 Dinesh Assistant is now running permanently!")
    print("🌐 Access the web interface at: http://localhost:8000")
    print("⌨️  Press Ctrl+C to stop the server when needed\n")

    try:
        server.run()
    except KeyboardInterrupt:
        print("\n👋 Dinesh Assistant is shutting down. Thanks for chatting!")
        sys.exit(0)
