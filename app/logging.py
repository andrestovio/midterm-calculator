import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging with a default file name if LOG_FILE is not set
log_file = os.getenv("LOG_FILE", "default.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),  # Logs to specified file
        logging.StreamHandler()         # Also logs to console
    ]
)

# Create a named logger
logger = logging.getLogger("Calculator")
