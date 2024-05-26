import logging

# Set up logging configuration
logging.basicConfig(
    filename='logs/xanadude.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
)

logger = logging.getLogger(__name__)