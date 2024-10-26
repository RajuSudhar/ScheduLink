import logging

def setup_logging(log_file: str = "app.log", log_level: str = "INFO"):
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # Output to console as well
        ]
    )

def log_info(message: str):
    logger = logging.getLogger(__name__)
    logger.info(message)

def log_error(message: str):
    logger = logging.getLogger(__name__)
    logger.error(message)

def log_warning(message: str):
    logger = logging.getLogger(__name__)
    logger.warning(message)

def log_debug(message: str):
    logger = logging.getLogger(__name__)
    logger.debug(message)

def log_critical(message: str):
    logger = logging.getLogger(__name__)
    logger.critical(message)

def log_exception(message: str):
    logger = logging.getLogger(__name__)
    logger.exception(message)

def log_to_file(message: str, log_file: str = "custom_log.log"):
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(log_file)
    logger.addHandler(file_handler)
    logger.info(message)
    logger.removeHandler(file_handler)
