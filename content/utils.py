import pandas as pd
import polars as pl

READ_ARGS = {
    "quote_char": None,
    "separator": "\t",
    "null_values": ["\\N", "nan"]
}

def polars_read_tsv_file(file_path):
    return pl.read_csv(f"{file_path}.tsv", **READ_ARGS)

def polars_scan_tsv_file(file_path):
    return pl.scan_csv(f"{file_path}.tsv", **READ_ARGS)

def pandas_read_tsv_file(file_path):
    return pd.read_csv(file_path + ".tsv", sep="\t", quoting=0, na_values=["\\N", "nan"])

def read_dataset_parquet_file(file_path):
    return pl.read_parquet(f"{file_path}.parquet")

def scan_dataset_parquet_file(file_path):
    return pl.scan_parquet(f"{file_path}.parquet")