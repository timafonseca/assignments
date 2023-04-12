"""Script to clean and save data"""

import argparse
import pathlib
from life_expectancy.cleaning import clean_data
from life_expectancy.loading_saving import load_data, save_data


FILE_NAME = "eu_life_expectancy_raw_test.tsv"
DIR_PATH = pathlib.Path(__file__).parent / "data"


def main(region_filter: str) -> None:
    """load_data, clean_data, and save_data in one function

    Args:
        region_filter (str): "PT"
    """
    file_path = DIR_PATH / FILE_NAME

    # load data
    df_load = load_data(file_path)

    # clean data
    df_clean = clean_data(df_load ,region_filter)

    return save_data(df_clean ,file_path)


if __name__=='__main__': # pragma: no cover

    parser = argparse.ArgumentParser(description='Clean and save life expectancy data')
    parser.add_argument('--region', '-r', default='PT', help='Region to filter on (default: PT)')
    args = parser.parse_args()

    main(args.region)
