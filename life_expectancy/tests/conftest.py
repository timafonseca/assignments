"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR, OUTPUT_DIR


@pytest.fixture(autouse=True)
def run_before_and_after_tests() -> None:
    """Fixture to execute commands before and after a test is run"""
    # Setup: fill with any logic you want

    # Teardown : fill with any logic you want
    file_path = OUTPUT_DIR / "pt_life_expectancy.csv"
    file_path.unlink(missing_ok=True)


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected_test.csv")


@pytest.fixture(scope="session")
def input_data() -> pd.DataFrame:
    """Fixture to load the test input of the cleaning script for a csv file"""
    return pd.read_csv(
        FIXTURES_DIR / "eu_life_expectancy_raw_test.tsv", sep="\t", na_values=[":"]
    )
