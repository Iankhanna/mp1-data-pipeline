import pandas as pd
from src import save_data

def test_save_data_creates_csv(sample_df, tmp_path):
    output_path = tmp_path / "clean.csv"
    saved_df = save_data(sample_df,output_path)
    assert output_path == saved_df
    df = pd.read_csv(output_path)
    assert len(df) == len(sample_df) and df.columns == sample_df.columns