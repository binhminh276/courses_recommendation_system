#!/usr/bin/env python3
"""
Script to train / fine-tune the Bi-Encoder Embedding model using Triplet Loss.
Usage:
    python scripts/run_train_embedding.py --epochs 5 --batch-size 32
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


def train_embedding(epochs: int, batch_size: int, learning_rate: float):
    logger.info("Starting Bi-Encoder Embedding model training...")
    logger.info(f"Hyperparameters: epochs={epochs}, batch_size={batch_size}, lr={learning_rate}")
    logger.info(f"Dataset directory: {DATA_DIR / 'embedding_datasets'}")
    logger.info(f"Output model directory: {MODELS_DIR / 'embedding_model'}")

    # TODO: Connect with src.embeddings.train module
    logger.info("Embedding model training finished.")


def main():
    parser = argparse.ArgumentParser(description="Train Bi-Encoder Embedding model.")
    parser.add_argument("--epochs", type=int, default=3, help="Number of training epochs.")
    parser.add_argument("--batch-size", type=int, default=32, help="Batch size.")
    parser.add_argument("--lr", type=float, default=2e-5, help="Learning rate.")
    args = parser.parse_args()
    train_embedding(epochs=args.epochs, batch_size=args.batch_size, learning_rate=args.lr)


if __name__ == "__main__":
    main()
