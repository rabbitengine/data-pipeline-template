import logging

import polars as pl

from config import settings

logger = logging.getLogger(__name__)


def load(df: pl.DataFrame) -> None:
    """Load data to output destination."""
    settings.output_dir.mkdir(exist_ok=True)
    path = settings.output_dir / settings.output_file
    df.write_parquet(path)
    logger.info(f"Loaded {len(df)} rows to {path}")
