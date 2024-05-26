from . import logger

def process_data(data):
    logger.info(f"Processing data: {data}")
    # Add core processing logic here
    result = f"Processed {data}"
    logger.info(f"Result: {result}")
    return result