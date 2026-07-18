"""
Income & Expenditure Management System (IEMS)

Application Entry Point
"""

import sys

from database.manager import DatabaseManager
from utils.logger import get_logger, setup_logging

logger = get_logger("app")


def main():
    setup_logging()

    logger.info("=" * 60)
    logger.info("Starting Income & Expenditure Management System")

    try:
        DatabaseManager.initialize()

        logger.info("Application initialized successfully.")
        logger.info("M1 completed successfully.")

    except Exception:
        logger.exception("Application startup failed.")
        sys.exit(1)

    finally:
        logger.info("Application shutting down.")
        logger.info("=" * 60)


if __name__ == "__main__":
    main()