from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Paths
    data_dir: Path = Field(default=Path("data"))
    output_dir: Path = Field(default=Path("output"))

    # Pipeline settings
    source_file: str = Field(default="orders.csv")
    output_file: str = Field(default="orders_enriched.parquet")


settings = Settings()
