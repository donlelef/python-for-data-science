import polars as pl
from polars.testing import assert_frame_equal
from processing.power_load_processing import aggregate_power_load_to_daily


def test_aggregates_power_load_correctly():
    df = pl.DataFrame({
        "Date": pl.Series(["2023-01-01 01:00", "2023-01-01 02:00", "2023-01-02"]).str.to_datetime(),
        "Load": [100, 150, 200]
    })
    result = aggregate_power_load_to_daily(df)
    expected = pl.DataFrame({
        "Date": pl.Series(["2023-01-01", "2023-01-02"]).str.to_datetime(),
        "Load": [250, 200]
    })
    assert_frame_equal(result, expected)

def test_handles_single_day():
    df = pl.DataFrame({
        "Date": pl.Series(["2023-01-01 01:00"]).str.to_datetime(),
        "Load": [100]
    })
    result = aggregate_power_load_to_daily(df)
    expected = pl.DataFrame({
        "Date": pl.Series(["2023-01-01"]).str.to_datetime(),
        "Load": [100]
    })
    assert_frame_equal(result, expected)

def test_handles_multiple_days():
    df = pl.DataFrame({
        "Date": pl.Series(["2023-01-01", "2023-01-02", "2023-01-03"]).str.to_datetime(),
        "Load": [100, 200, 300]
    })
    result = aggregate_power_load_to_daily(df)
    expected = pl.DataFrame({
        "Date": pl.Series(["2023-01-01", "2023-01-02", "2023-01-03"]).str.to_datetime(),
        "Load": [100, 200, 300]
    })
    assert_frame_equal(result, expected)
