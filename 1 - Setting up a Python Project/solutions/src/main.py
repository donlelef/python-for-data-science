import logging
from pathlib import Path

from output.power_load_output import write_output
from paths import RAW_DATA_DIR, OUTPUT_PATH
from processing.power_load_processing import aggregate_power_load_to_daily
from src.sourcing.power_load_sourcing import read_power_load


def main():
    logging.basicConfig(
        level=logging.INFO, format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    )

    input_path = RAW_DATA_DIR / 'power_load.csv'
    output_path = OUTPUT_PATH / 'power_load_daily.csv'

    process_power_load(input_path, output_path)


def process_power_load(input_path: Path, output_path: Path):
    logging.info(f"Reading power load data from {input_path}...")
    raw_df = read_power_load(input_path)
    logging.info(f"Read {len(raw_df)} rows.")
    logging.info("Aggregating power load data to daily...")
    processed_df = aggregate_power_load_to_daily(raw_df)
    logging.info(f"Aggregated to {len(processed_df)} rows.")
    logging.info("Writing output...")
    write_output(processed_df, output_path)
    logging.info("Output written.")


if __name__ == '__main__':
    main()