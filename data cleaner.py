"""
Data cleaner with Pandas, Pathlib and Os.

The program drops null values, removes duplicates and corrects the datatypes from a specific dataset.

author: Pferdeliebe
"""

import pandas as pd
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

FILE_NAME = "data/my_data.csv"

def read_data():
    """Read the data "my_data.csv" in the folder data."""
    df = pd.read_csv(FILE_NAME)
    return df


def drop_null_values(df):
    """Show missing values and drops null values."""
    print("Head:\n", df.head())
    print("Missing values:\n", df.isna().sum())
    print("Shape:", df.shape)
    df_new = df.dropna(axis="index", thresh=6).copy()
    print("Head:", df_new.head())
    print("Missing values", df_new.isna().sum())
    return df_new

def remove_duplicates(df_new):
    "Removes duplicates from the dataset."
    return df_new.drop_duplicates()


def type_corrections(df_new):
    """
    Changes numbers into numeric numbers and makes mistakes to NaN-values.
    Changes the datatypes.
    """
    print("Datatypes",df_new.dtypes)

    df_new["Order ID"] = pd.to_numeric(df_new["Order ID"], errors="coerce")
    df_new["Order ID"]= df_new["Order ID"].astype("Int64")

    df_new["Quantity Ordered"] = pd.to_numeric(df_new["Quantity Ordered"], errors="coerce")
    df_new["Quantity Ordered"]= df_new["Quantity Ordered"].astype("Int64")

    df_new["Price Each"] = pd.to_numeric(df_new["Price Each"], errors="coerce")
    df_new["Price Each"]= df_new["Price Each"].astype("float64")
    print("Datatypes",df_new.dtypes)
    return df_new


def main():
    df = read_data()

    df_new = drop_null_values(df)
    df_new = remove_duplicates(df_new)
    type_corrections(df_new)

if __name__ == "__main__":
    main()

