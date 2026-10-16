import pandas as pd
import pytest
from src.data_processor import (handle_missing, remove_duplicates, remove_outliers)

def test_remove_duplicates(sample_df):
    df = remove_duplicates(sample_df)
    assert len(df) == 98

def test_handle_missing_rows(sample_df):
    df = sample_df[["rating"]].copy()
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df = handle_missing(df,axis="rows")
    assert len(df) == 97

def test_remove_outliers_iqr(sample_df):
    df = sample_df[["rating"]].copy()
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df = df.dropna()
    df = remove_outliers(df,["rating"],method="iqr",threshold=1.5)
    assert len(df) == 95

def test_remove_outliers_zscore(sample_df):
    df = sample_df[["rating"]].copy()
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df = df.dropna()
    df = remove_outliers(df,["rating"],method="zscore",threshold=3)
    assert len(df) == 95

def test_remove_outliers_with_unsupported_method(sample_df):
    with pytest.raises(ValueError):
        remove_outliers(sample_df,["rating"],method="unknown_method",threshold=3)