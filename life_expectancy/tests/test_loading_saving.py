"""Tests for the loading and saving module"""
import pandas as pd
from unittest import mock

from life_expectancy.cleaning import load_data, save_data


def test_load_data(loaded_data_test):
    """Test if the load function works"""

    loaded_data=load_data()

    pd.testing.assert_frame_equal(
        loaded_data, loaded_data_test
    )

@mock.patch("pandas.DataFrame.to_csv")
def test_save_data(mock_to_csv, pt_life_expectancy_expected):
    """Test if the load function works"""

    output_file_path = "./life_expectancy/data/pt_life_expectancy.csv"
    save_data(pt_life_expectancy_expected)

    mock_to_csv.assert_called_with(output_file_path, index=False)