import polars as pl

def aggregate_power_load_to_daily(power_load: pl.DataFrame) -> pl.DataFrame:
    return power_load.group_by_dynamic(pl.col("Date"), every="1d").agg(pl.col("Load").sum().alias("Load"))