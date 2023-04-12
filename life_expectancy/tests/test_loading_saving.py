"""Tests for the loading and saving module"""

from unittest import mock
import pandas as pd

from life_expectancy.loading_saving import load_data, save_data
from . import FIXTURES_DIR

@mock.patch("life_expectancy.loading_saving.pd.read_csv")
def test_load_data(mock_read,input_data):
    """Test if the load function works"""

    mock_read.return_value = input_data

    file_path = FIXTURES_DIR / "eu_life_expectancy_raw_test.tsv"

    loaded_data = load_data(file_path)

    pd.testing.assert_frame_equal(loaded_data, input_data)

    mock_read.assert_called_once_with(file_path ,  sep="\t")

@mock.patch("life_expectancy.loading_saving.pd.DataFrame.to_csv")
def test_save_data(mock_to_csv, pt_life_expectancy_expected):
    """Test if the save function works"""

    mock_to_csv.side_effect = print("saved", end="")

    save_data(pt_life_expectancy_expected, FIXTURES_DIR / "fixtures")

    mock_to_csv.assert_called_with(
        FIXTURES_DIR / "pt_life_expectancy.csv", index=False
    )