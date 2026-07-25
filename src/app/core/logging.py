from pathlib import Path
from loguru import logger
from app.config import settings

PROJECT_ROOT = Path(__file__).resolve().parents[3]
LOG_ROOT = PROJECT_ROOT / "logs"

def configure_logging() -> None:
    """Configure application logging."""
    LOG_ROOT.mkdir(exist_ok=True)
    logger.remove()

    logger.add(
        sink=lambda msg: print(msg, end=""),
        level=settings.log_level,
        colorize=True,
    )

    logger.add(
        LOG_ROOT / "application" / "application.log",
        rotation=settings.log_rotation,
        retention=f"{settings.log_retention_days} days",
        level=settings.log_level,
        enqueue=True,
    )

    logger.add(
        LOG_ROOT / "errors" / "errors.log",
        level="ERROR",
        rotation=settings.log_rotation,
        retention=f"{settings.log_retention_days} days",
        enqueue=True,
    )