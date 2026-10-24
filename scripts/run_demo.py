#!/usr/bin/env python3
"""
Interactive or web-based demo script for testing Course recommendations from JD and CV.
Usage:
    python scripts/run_demo.py --mode cli
"""

import argparse
import logging
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def run_demo(mode: str):
    logger.info(f"Launching Courses Recommendation Demo in [{mode}] mode...")
    logger.info(f"Project root: {PROJECT_ROOT}")

    if mode == "cli":
        print("\n=== DEMO: HỆ THỐNG GỢI Ý KHÓA HỌC (COURSES RECOMMENDATION) ===")
        print("1. Nhập JD / Yêu cầu công việc")
        print("2. Trích xuất Thực thể & Kỹ năng (NER)")
        print("3. Tìm kiếm Hybrid (Dense Embedding + BM25)")
        print("4. Xuất danh sách khóa học phù hợp nhất\n")
    else:
        logger.info(f"Starting web UI demo...")


def main():
    parser = argparse.ArgumentParser(description="Run Courses Recommendation System Demo.")
    parser.add_argument(
        "--mode",
        choices=["cli", "web"],
        default="cli",
        help="Demo mode: command line interface (cli) or web app."
    )
    args = parser.parse_args()
    run_demo(args.mode)


if __name__ == "__main__":
    main()
