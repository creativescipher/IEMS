"""
Income & Expenditure Management System (IEMS)

Application Entry Point
"""

import sys

from database.connection import check_connection
from database.schema import initialize_database
from utils.logger import get_logger, setup_logging

logger = get_logger("app")


def main():

    setup_logging()

    logger.info("=" * 60)
    logger.info("Starting Income & Expenditure Management System")

    if not check_connection():
        logger.critical("Database connection failed.")
        sys.exit(1)

    initialize_database()

    logger.info("Database initialized.")

    logger.info("Application initialized successfully.")
    logger.info("M1 completed successfully.")
    logger.info("Application shutting down.")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()