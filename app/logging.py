import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("calculator.log"),
        logging.StreamHandler()
    ]
)

# Create a named logger
logger = logging.getLogger("Calculator")
