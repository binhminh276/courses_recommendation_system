#!/usr/bin/env python3
"""
Script to run the ETL pipeline: cleaning, normalizing, and structuring data.
Usage:
    python scripts/run_etl_pipeline.py --target all
    python scripts/run_etl_pipeline.py --target courses
    python scripts/run_etl_pipeline.py --target jobs
    python scripts/run_etl_pipeline.py --target cv
"""

import argparse
import logging
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def run_etl(target: str):
    logger.info(f"Starting ETL pipeline for target: {target}")
    logger.info(f"Project root: {PROJECT_ROOT}")

    if target in ("courses", "all"):
        logger.info("Processing courses data -> data/processed/courses/")
        # TODO: Link to src.preprocessing.courses

    if target in ("jobs", "all"):
        logger.info("Processing job data -> data/processed/jobs/")
        # TODO: Link to src.preprocessing.jobs

    if target in ("cv", "all"):
        logger.info("Processing CV data -> data/processed/cv/")
        # TODO: Link to src.preprocessing.cv

    logger.info("ETL pipeline completed successfully.")


def main():
    parser = argparse.ArgumentParser(description="Run ETL preprocessing pipeline.")
    parser.add_argument(
        "--target",
        choices=["courses", "jobs", "cv", "all"],
        default="all",
        help="Target data entity to process."
    )
    args = parser.parse_args()
    run_etl(args.target)


if __name__ == "__main__":
    main()
