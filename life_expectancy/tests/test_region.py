"""
module that tests the class function created in the country enum
"""
import pandas as pd
from life_expectancy.region import Region

def test_region_list():
    """Test function to assert the valid countries output list"""
    list_region_expected= [
        'AT',
        'BE',
        'BG',
        'CH',
        'CY',
        'CZ',
        'DK',
        'EE',
        'EL',
        'ES',
        'EU',
        'FI',
        'FR',
        'HR',
        'HU',
        'IS',
        'IT',
        'LI',
        'LT',
        'LU',
        'LV']

    list_region_actual= Region.list_valid_region(
        pd.read_csv("life_expectancy/tests/fixtures/eu_life_expectancy_json_test.csv"),
        "region")

    assert list_region_expected == list_region_actual
