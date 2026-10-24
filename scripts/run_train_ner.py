#!/usr/bin/env python3
"""
Script to train / fine-tune the NER model for extracting entities from JD, CV, and Course descriptions.
Usage:
    python scripts/run_train_ner.py --config configs/ner_config.yaml
"""

import argparse
import logging
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def train_ner(config_path: str = None):
    logger.info("Starting NER model training...")
    logger.info(f"Using dataset from: {DATA_DIR / 'ner_datasets'}")
    logger.info(f"Target model save directory: {MODELS_DIR / 'ner_model'}")

    # TODO: Connect with src.ner.train module
    logger.info("NER training finished.")


def main():
    parser = argparse.ArgumentParser(description="Train Named Entity Recognition (NER) model.")
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Path to YAML configuration file for NER training."
    )
    args = parser.parse_args()
    train_ner(args.config)


if __name__ == "__main__":
    main()
