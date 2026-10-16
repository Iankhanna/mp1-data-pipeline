from logging import config

import pytest
from src import validate_dataframe

def test_validate_dataframe_removes_invalid_ratings(sample_df):
    """Set the required and numeric column names and assert the correct number of rows and columns"""
    required_columns = config["required_columns"]
    numeric_columns = config["numeric_columns"]
    validated_df = validate_dataframe(sample_df,required_columns,numeric_columns)
    assert len(validated_df) == 98 and validated_df.shape[1] == 5

def test_validate_dataframe_with_missing_column(sample_df):
    with pytest.raises(ValueError):
        validate_dataframe(sample_df,["price"],["rating"])