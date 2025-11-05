"""Monitor and maintain the Dinesh Assistant service."""

import logging
import os
import subprocess
import sys
import time
from pathlib import Path

import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("service_monitor.log"),
        logging.StreamHandler(sys.stdout),
    ],
)


def check_health() -> bool:
    """Check if the service is healthy."""
    try:
        response = requests.get("http://localhost:8000/health")
        return response.status_code == 200
    except requests.RequestException:
        return False


def restart_service() -> None:
    """Restart the chatbot service."""
    logging.info("Attempting to restart service...")
    try:
        # Kill any existing process
        subprocess.run(["pkill", "-f", "uvicorn"])
        time.sleep(2)  # Wait for process to die

        # Start the service
        env = os.environ.copy()
        env["PYTHONPATH"] = str(Path(__file__).parent)

        subprocess.Popen(
            ["python3", "src/web/app.py"], env=env, cwd=str(Path(__file__).parent)
        )

        logging.info("Service restart initiated")
    except Exception as e:
        logging.error(f"Failed to restart service: {e}")


def main():
    """Main monitoring loop."""
    consecutive_failures = 0
    max_failures = 3
    check_interval = 60  # Check every minute

    logging.info("Starting service monitor...")

    while True:
        if not check_health():
            consecutive_failures += 1
            logging.warning(
                f"Health check failed ({consecutive_failures}/{max_failures})"
            )

            if consecutive_failures >= max_failures:
                logging.error("Maximum failures reached, attempting restart")
                restart_service()
                consecutive_failures = 0
                time.sleep(30)  # Give service time to start
        else:
            if consecutive_failures > 0:
                logging.info("Service recovered")
            consecutive_failures = 0

        time.sleep(check_interval)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Monitor shutting down")
        sys.exit(0)
