import logging

import polars as pl

logger = logging.getLogger(__name__)


def transform(df: pl.DataFrame) -> pl.DataFrame:
    """Transform data: add calculated fields."""
    df = df.with_columns([
        # Calculate total
        (pl.col("quantity") * pl.col("price")).round(2).alias("total"),
        # Extract month
        pl.col("order_date").str.to_date().dt.month().alias("order_month"),
    ])
    logger.info(f"Transformed {len(df)} rows")
    return df
