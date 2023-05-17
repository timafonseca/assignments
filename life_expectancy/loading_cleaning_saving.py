"""Script to clean and save data"""

import pathlib
import json
import pandas as pd
from life_expectancy.region import Region


class DataLoader:
    """Abstract interface for loading data"""
    def load_data(self, path: pathlib.Path) -> pd.DataFrame:
        """Read data function"""

    def clean_data(self, df_input: pd.DataFrame, region: Region) -> pd.DataFrame:
        """Clean data function"""

    def save_data(self, df_output: pd.DataFrame, path: pathlib.Path) -> None:
        """Save a data file"""


class ExcelDataLoader(DataLoader):
    """Concrete implementation of DataLoader for loading Excel data"""
    def load_data(self, path: pathlib.Path) -> pd.DataFrame:
        """Read csv data function"""
        df_input = pd.read_csv(path, sep="\t")
        return df_input

    def clean_data(self, df_input: pd.DataFrame, region: Region) -> pd.DataFrame:
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

        df_output = df_col_fix[df_col_fix["region"] == region.value]
        return df_output

    def save_data(self, df_output: pd.DataFrame, path: pathlib.Path) -> None:
        """save data into a file

        Args:
            df_output (pd.DataFrame): output data
        """

        df_output.to_csv(path.parent / "pt_life_expectancy.csv", index=False)


class JsonDataLoader(DataLoader):
    """Concrete implementation of DataLoader for loading JSON data"""
    def load_data(self, path: pathlib.Path) -> pd.DataFrame:
        """Read json data function"""
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
        df_input = pd.json_normalize(data)
        return df_input

    def clean_data(self, df_input: pd.DataFrame, region: Region) -> pd.DataFrame:
        """Clean json dataframe"""

        df_clean = df_input[
            ["unit", "sex", "age", "country", "year", "life_expectancy"]
        ]
        df_clean = df_clean.rename(
            columns={"country": "region", "life_expectancy": "value"}
        )
        return df_clean

    def save_data(self, df_output: pd.DataFrame, path: pathlib.Path) -> None:
        """save data into a file

        Args:
            df_output (pd.DataFrame): output data
        """

        df_output.to_csv(path.parent / "eu_life_expectancy.csv", index=False)
