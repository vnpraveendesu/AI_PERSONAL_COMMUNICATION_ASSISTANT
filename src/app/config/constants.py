from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
LOG_DIR = PROJECT_ROOT / "logs"
DATABASE_DIR = DATA_DIR / "database"


SUPPORTED_EMAIL_PROVIDERS = ["gmail", "outlook"]

SUPPORTED_LEAVE_STATUS = [
    "reported",
    "pending_confirmation",
    "approved",
    "rejected",
    "completed",
    "cancelled",
]
