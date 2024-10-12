from pathlib import Path

import polars as pl


def read_power_load(file_path: Path) -> pl.DataFrame:
    return pl.read_csv(file_path, try_parse_dates=True)