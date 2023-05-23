"""Script to clean and save data"""


import argparse
from pathlib import Path

from life_expectancy.loading_cleaning_saving import (
    ExcelDataLoader,
    JsonDataLoader
)
from life_expectancy.region import Region


def main(region_filter: Region, file_path : Path) -> None:
    """load_data, clean_data, and save_data in one function

    Args:
        region_filter (str): "PT"
    """

    # load data
    extension = file_path.suffix.lower()

    # Choose the appropriate DataLoader based on the file extension
    if extension in {".csv", ".tsv"}:
        loader = ExcelDataLoader()
        df_load = loader.load_data(file_path)

        # clean data
        df_clean = loader.clean_data( df_load ,region_filter)

        loader.save_data(df_clean ,file_path)

    elif extension == ".json":
        loader = JsonDataLoader()
        df_load = loader.load_data(file_path)

        df_clean = loader.clean_data(df_load ,region_filter)

        loader.save_data(df_clean ,file_path)


    else:
        raise ValueError(f"Unsupported file extension: {extension}")

    return df_clean


if __name__=='__main__': # pragma: no cover

    parser = argparse.ArgumentParser(description='Clean and save life expectancy data')
    parser.add_argument(
        '--region',
        type=Region,
        default=Region.PT,
        help='Region to filter on (default: PT)')

    parser.add_argument(
        "--file_path",
        type=Path,
        default=None,
        help="The input file containing life expectancy data (default: eu_life_expectancy_raw.tsv)")
    args = parser.parse_args()

    if args.file_path is None:
        FILE_NAME ="eu_life_expectancy_raw.tsv"
        DIR_PATH = Path(__file__).parent / "data"
        args.file_path = DIR_PATH / FILE_NAME

    main(args.region, args.file_path)
