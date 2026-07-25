from loguru import logger

def get_logger(component: str):
    return logger.bind(component=component)