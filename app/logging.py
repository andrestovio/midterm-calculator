import logging
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Configure logging
log_file = os.getenv("LOG_FILE", "default.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# Create a named logger
logger = logging.getLogger("Calculator")
