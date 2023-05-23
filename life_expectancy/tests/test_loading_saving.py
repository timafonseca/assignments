"""Tests for the loading and saving module"""

from unittest import mock
import pandas as pd

from life_expectancy.loading_cleaning_saving import (
    ExcelDataLoader,
    JsonDataLoader
)
from . import FIXTURES_DIR

@mock.patch("life_expectancy.loading_cleaning_saving.pd.read_csv")
def test_load_data_csv(mock_read,input_data_csv):
    """Test if the load function works"""

    mock_read.return_value = input_data_csv

    file_path = FIXTURES_DIR / "eu_life_expectancy_raw_test.tsv"

    # load data
    extension = file_path.suffix.lower()

    # Choose the appropriate DataLoader based on the file extension
    if extension in {".csv", ".tsv"}:
        loader = ExcelDataLoader()
        loaded_data = loader.load_data(file_path)

    elif extension == ".json":
        loader = JsonDataLoader()
        loaded_data = loader.load_data(file_path)

    else:
        raise ValueError(f"Unsupported file extension: {extension}")

    pd.testing.assert_frame_equal(loaded_data, input_data_csv)

    mock_read.assert_called_once_with(file_path, sep="\t")

@mock.patch("life_expectancy.loading_cleaning_saving.JsonDataLoader.load_data")
def test_load_data_json(mock_read,input_data_json):
    """Test if the load function works"""

    mock_read.return_value = input_data_json

    file_path = FIXTURES_DIR / "eurostat_life_expect_test.json"

    # load data
    extension = file_path.suffix.lower()

    # Choose the appropriate DataLoader based on the file extension
    if extension in {".csv", ".tsv"}:
        loader = ExcelDataLoader()
        loaded_data = loader.load_data(file_path)

    elif extension == ".json":
        loader = JsonDataLoader()
        loaded_data = loader.load_data(file_path)

    else:
        raise ValueError(f"Unsupported file extension: {extension}")

    pd.testing.assert_frame_equal(loaded_data, input_data_json)

    mock_read.assert_called_once_with(file_path)

@mock.patch("life_expectancy.loading_cleaning_saving.pd.DataFrame.to_csv")
def test_save_data_csv(mock_to_csv, pt_life_expectancy_expected):
    """Test if the save function works"""

    mock_to_csv.side_effect = print("saved", end="")

    loader = ExcelDataLoader()
    loader.save_data(pt_life_expectancy_expected, FIXTURES_DIR / "fixtures")

    mock_to_csv.assert_called_with(
        FIXTURES_DIR / "pt_life_expectancy.csv", index=False
    )

@mock.patch("life_expectancy.loading_cleaning_saving.pd.DataFrame.to_csv")
def test_save_data_json(mock_to_csv, eu_life_expectancy_expected_json):
    """Test if the save function works"""

    mock_to_csv.side_effect = print("saved", end="")

    loader = JsonDataLoader()
    loader.save_data(eu_life_expectancy_expected_json, FIXTURES_DIR / "fixtures")

    mock_to_csv.assert_called_with(
        FIXTURES_DIR / "eu_life_expectancy.csv", index=False
    )
