"""Tests for the cleaning module"""

from unittest.mock import patch
import pandas as pd
from life_expectancy.main import main
from life_expectancy.region import Region
from . import OUTPUT_DIR

@patch("life_expectancy.main.ExcelDataLoader.load_data")
@patch("life_expectancy.main.ExcelDataLoader.save_data")
def test_main_csv(
    mock_save, mock_load, pt_life_expectancy_expected, input_data_csv
):
    """Run the `clean_data` function and compare the output to the expected output"""

    mock_load.return_value = input_data_csv

    mock_save.side_effect = print("saved", end="")

    file_path = OUTPUT_DIR / "eu_life_expectancy_raw_test.tsv"

    actual = main(Region.PT,file_path).reset_index(drop=True)

    mock_load.assert_called_once_with(file_path)

    mock_save.assert_called_once()

    pd.testing.assert_frame_equal(
        actual, pt_life_expectancy_expected
    )

@patch("life_expectancy.main.JsonDataLoader.load_data")
@patch("life_expectancy.main.JsonDataLoader.save_data")
def test_main_json(
    mock_save, mock_load, eu_life_expectancy_expected_json, input_data_json
):
    """Run the `clean_data` function and compare the output to the expected output"""

    mock_load.return_value = input_data_json

    mock_save.side_effect = print("saved", end="")

    file_path = OUTPUT_DIR / "eurostat_life_expect_test.json"

    actual = main(Region.PT,file_path).reset_index(drop=True)

    mock_load.assert_called_once_with(file_path)

    mock_save.assert_called_once()

    pd.testing.assert_frame_equal(
        actual, eu_life_expectancy_expected_json
    )
