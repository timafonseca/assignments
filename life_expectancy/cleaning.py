"""Script to clean and save data"""

import argparse
import logging
import pandas as pd
#from pathlib import Path


def load_data() -> pd.DataFrame:
    """read and return the input data

    Returns:
        pd.DataFrame: input data
    """

    #root = Path()
    #print(root)

    df_input = pd.read_csv(
        "./life_expectancy/data/eu_life_expectancy_raw.tsv", sep="\t"
    )

    return df_input



def clean_data(df_input : pd.DataFrame , region: str = "PT") -> pd.DataFrame:
    """Load"eu_life_expectancy_raw.tsv" file in the "data" folder
    unpivot the data into a long format with columns for unit, sex, age, region, year, and value
    convert the year column to an integer
    convert the value column to a float and remove any NaN values
    filter the data to only include records where the region is Portugal (PT)
    Saved "pt_life_expectancy.csv" with the output.

    Args:
        region_filter (str): "PT"
    """

    df_input[["unit", "sex", "age", "region"]] = df_input[
        "unit,sex,age,geo\\time"
    ].str.split(",", expand=True)

    df_input = df_input.drop(columns=["unit,sex,age,geo\\time"])

    df_col_fix = pd.melt(
        df_input,
        id_vars=["unit", "sex", "age", "region"],
        var_name="year"
    )
    df_col_fix = df_col_fix.dropna()

    df_col_fix["year"] = df_col_fix["year"].astype(int)
    df_col_fix["value"] = df_col_fix["value"].str.extract(r"(\d+\.?\d*)").astype(float)
    df_col_fix["value"] = pd.to_numeric(df_col_fix["value"], errors="coerce")
    df_col_fix = df_col_fix.dropna()

    df_output = df_col_fix[df_col_fix["region"] == region]
    return df_output

def save_data(df_output:pd.DataFrame):
    """save data into a file

    Args:
        df_output (pd.DataFrame): output data 
    """

    df_output.to_csv("./life_expectancy/data/pt_life_expectancy.csv", index=False)

    logging.info("Successfully saved data")


def main(region_filter: str) -> None:
    """load_data, clean_data, and save_data in one function

    Args:
        region_filter (str): "PT"
    """

    save_data(clean_data(load_data(), region=region_filter))


if __name__=='__main__': # pragma: no cover

    parser = argparse.ArgumentParser(description='Clean and save life expectancy data')
    parser.add_argument('--region', '-r', default='PT', help='Region to filter on (default: PT)')
    args = parser.parse_args()

    main(args.region)
