import logging

from extract import extract
from transform import transform
from load import load

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def run() -> None:
    """Run the complete ETL pipeline."""
    logger.info("Starting pipeline...")

    # Extract
    df = extract()

    # Transform
    df = transform(df)

    # Load
    load(df)

    logger.info("Pipeline complete!")


if __name__ == "__main__":
    run()
