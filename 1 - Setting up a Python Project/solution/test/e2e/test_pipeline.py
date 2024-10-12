from main import process_power_load
from paths import RAW_DATA_DIR


def test_process_power_load(tmp_path):
    input_path = RAW_DATA_DIR / 'power_load.csv'
    output_path = tmp_path / 'power_load_daily.csv'

    process_power_load(input_path, output_path)

    assert output_path.exists()


