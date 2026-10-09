# MP1 Data Processing Pipeline Explanation
This project was created to be a Python data processing pipeline. The pipeline can do several things like loading, validating, cleaning, and saving different data. The pipeline also uses a YAML configuration file in order to control validation and cleaning operations. The data_loaders.py loads all of the input files and the and  data_validator.py checks all the columns while removing any rows containing invalid numeric values. data_processor.py module removes duplicates, handles missing values, and removes outliers. The data_output.py module saves cleaned data as a CSV file, while utils.py provides logging and input file validation. The pipeline.py file connects these modules and runs the complete workflow.

## Example Command
```bash
python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```

## Results
The pipeline loaded 100 rows, removed 2 rows with invalid numeric values, 2 duplicate rows, 2 rows with missing values, and 2 outliers. The final cleaned dataset contains 92 rows and 5 columns, saved to output/clean.csv.