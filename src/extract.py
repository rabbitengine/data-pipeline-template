import logging

import polars as pl

from config import settings

logger = logging.getLogger(__name__)


def extract() -> pl.DataFrame:
    """Extract data from source CSV."""
    path = settings.data_dir / settings.source_file
    df = pl.read_csv(path)
    logger.info(f"Extracted {len(df)} rows from {path}")
    return df
