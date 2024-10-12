from pathlib import Path

import polars as pl


def write_output(df: pl.DataFrame, file_path: Path) -> None:
    df.write_csv(file_path)