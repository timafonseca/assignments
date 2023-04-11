"""Script to clean and save data"""

import pandas as pd
import pathlib


def load_data(path: pathlib.Path) -> pd.DataFrame:
    """Read and return the input data
    Param: 
        path: Path to csv file
    Returns:
        pd.DataFrame: input data
    """

    df_input = pd.read_csv(path, sep="\t")

    return df_input


def save_data(df_output: pd.DataFrame, path: pathlib.Path) -> pd.DataFrame:
    """save data into a file

    Args:
        df_output (pd.DataFrame): output data 
    """

    df_output.to_csv(path.parent / "pt_life_expectancy.csv", index=False)
