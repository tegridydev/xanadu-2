from . import logger
from .logic import process_data

def handle_input(event):
    logger.info(f"Handling input: {event}")
    result = process_data(event)
    logger.info(f"Input handled, result: {result}")
    return result