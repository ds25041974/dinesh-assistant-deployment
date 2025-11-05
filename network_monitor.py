"""Network connectivity checker for OpenAI service."""

import logging
import socket
import time
from typing import Dict, List, Optional, Tuple, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="network_monitor.log",
)


def check_openai_connection() -> Dict[str, Union[bool, str]]:
    """Check connection to OpenAI services."""
    try:
        # Try to connect to OpenAI's API
        socket.create_connection(("api.openai.com", 443), timeout=3)
        return {"status": True, "message": "Connection to OpenAI is available"}
    except OSError as e:
        return {"status": False, "message": f"Cannot connect to OpenAI: {str(e)}"}


def monitor_network() -> None:
    """Monitor network connectivity and log status."""
    while True:
        result = check_openai_connection()
        if result["status"]:
            logging.info(result["message"])
        else:
            logging.warning(result["message"])
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    try:
        monitor_network()
    except KeyboardInterrupt:
        logging.info("Network monitoring stopped")
