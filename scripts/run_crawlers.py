#!/usr/bin/env python3
"""
Script to orchestrate data crawlers for Courses and Jobs.
Usage:
    python scripts/run_crawlers.py --source all
    python scripts/run_crawlers.py --source courses
    python scripts/run_crawlers.py --source jobs
"""

import argparse
import logging
from pathlib import Path

# Resolve PROJECT_ROOT regardless of execution location
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def run_crawlers(source: str):
    logger.info(f"Starting crawler execution for source: {source}")
    logger.info(f"Project root resolved to: {PROJECT_ROOT}")
    raw_dir = DATA_DIR / "raw"
    logger.info(f"Raw data target directory: {raw_dir}")

    if source in ("courses", "all"):
        logger.info("Executing Course crawlers (Coursera, Udemy, edX, DataCamp, FutureLearn)...")
        # TODO: Link to src.crawlers.courses modules

    if source in ("jobs", "all"):
        logger.info("Executing Job crawlers (TopCV, ITviec, VietnamWorks, CareerViet, etc.)...")
        # TODO: Link to src.crawlers.jobs modules

    logger.info("Crawler execution completed.")


def main():
    parser = argparse.ArgumentParser(description="Run Course and Job crawlers.")
    parser.add_argument(
        "--source",
        choices=["courses", "jobs", "all"],
        default="all",
        help="Target data source to crawl (courses, jobs, or all)."
    )
    args = parser.parse_args()
    run_crawlers(args.source)


if __name__ == "__main__":
    main()
