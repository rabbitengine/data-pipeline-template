# Data Pipeline Template

A minimal ETL pipeline template using Polars and Pydantic. Clone, customize, and build.

## Quick Start

**1. Install pipx and hatch:**

```bash
sudo apt-get install pipx
pipx install hatch
```

**2. Run the pipeline:**

```bash
hatch run pipeline
```

That's it. Output lands in `output/orders_enriched.parquet`.

## Structure

```
data-pipeline-template/
├── data/
│   └── orders.csv           # Sample source data
├── src/
│   ├── config.py            # Pydantic settings
│   ├── extract.py           # Read from source
│   ├── transform.py         # Transform with Polars
│   ├── load.py              # Write to destination
│   └── pipeline.py          # Orchestrate ETL
├── config.yaml              # Pipeline config
└── pyproject.toml           # Dependencies & scripts
```

## Customize

1. Replace `data/orders.csv` with your data
2. Edit `src/transform.py` to add your logic
3. Update `src/load.py` for your destination (BigQuery, Snowflake, etc.)

## Stack

- **Polars** - Fast DataFrame library
- **Pydantic** - Config validation
- **Hatch** - Python project manager
