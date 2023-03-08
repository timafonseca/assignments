"""Script to clean and save data"""

import pandas as pd
import argparse

def clean_data(region: str = "PT") -> pd.DataFrame:
    """Load"eu_life_expectancy_raw.tsv" file in the "data" folder
    unpivot the data into a long format with columns for unit, sex, age, region, year, and value
    convert the year column to an integer
    convert the value column to a float and remove any NaN values
    filter the data to only include records where the region is Portugal (PT)
    Saved "pt_life_expectancy.csv" with the output.
    """
    df_input = pd.read_csv(
        "./life_expectancy/data/eu_life_expectancy_raw.tsv", sep="\t"
    )

    df_input[["unit", "sex", "age", "region"]] = df_input[
        "unit,sex,age,geo\\time"
    ].str.split(",", expand=True)

    df_input = df_input.drop(columns=["unit,sex,age,geo\\time"])

    df_col_fix = pd.melt(
        df_input,
        id_vars=["unit", "sex", "age", "region"],
        var_name="year",
        value_name="value",
    )

    df_col_fix["year"] = df_col_fix["year"].astype(int)

    df_col_fix["value"] = pd.to_numeric(df_col_fix["value"], errors="coerce")

    df_output = df_col_fix.loc[df_col_fix["region"] == region]

    df_output.to_csv("./life_expectancy/data/pt_life_expectancy.csv", index=False)


if __name__=='__main__': # pragma: no cover

    parser = argparse.ArgumentParser(description='Clean and save life expectancy data')
    parser.add_argument('--region', '-r', default='PT', help='Region to filter on (default: PT)')
    args = parser.parse_args()

    clean_data(args.region)

