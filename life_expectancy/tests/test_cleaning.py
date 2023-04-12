"""Tests for the cleaning module"""

from unittest.mock import patch
import pandas as pd
from life_expectancy.main import main
from . import OUTPUT_DIR

@patch("life_expectancy.main.load_data")
@patch("life_expectancy.main.save_data")
def test_main(
    mock_save, mock_load, pt_life_expectancy_expected, input_data
):
    """Run the `clean_data` function and compare the output to the expected output"""

    mock_load.return_value = input_data

    mock_save.side_effect = print("saved", end="")

    file_path = OUTPUT_DIR / "eu_life_expectancy_raw_test.tsv"

    actual = main("PT").reset_index(drop=True)

    mock_load.assert_called_once_with(file_path)

    mock_save.assert_called_once()

    pd.testing.assert_frame_equal(
        actual, pt_life_expectancy_expected
    )
