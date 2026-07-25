from app.core.logging import configure_logging
from app.core.logger_factory import get_logger


def test_logging():
    configure_logging()
    logger = get_logger("test")
    logger.info("Logging test")
    assert True
