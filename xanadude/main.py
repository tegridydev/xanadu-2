from gui.main_window import main
from core.startup import initialize_system
from core import logger

if __name__ == '__main__':
    logger.info("Starting Xanadude application.")
    initialize_system()
    main()
    logger.info("Xanadude application has exited.")