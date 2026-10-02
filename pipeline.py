"""
Data Processing Pipeline - CLI Template

DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
import sys
from pathlib import Path
from data_processor import process_data, create_cleaning_report
from data_loaders import load_data

logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    level = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(level=level,format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",datefmt="%H:%M:%S")


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Data Processing Pipeline"
    )

    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to the input file"
    )
   
    parser.add_argument(
    "--config",
    required=True,
    help="Path for the YAML configuration file"
    )

    parser.add_argument(
        "--output", "-o",
        required=True,
        help="Path to the output file"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()
    return args


def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    p = Path(filepath)

    if not p.is_file():
        logger.error(f"Input file not found: {filepath}")
        return False

    logger.info(f"Input file validated: {filepath}")
    return True


def main():
    """Main pipeline function."""
    args = parse_arguments()

    setup_logging(args.verbose)

    logger.debug(f"Arguments parsed: input={args.input}, config={args.config}, output={args.output}")

    if not validate_input(args.input):
        sys.exit(1)
        
    if not validate_input(args.config):
        sys.exit(1)

    try:
        df = load_data(args.input)
        config = load_data(args.config)
    except ValueError as error:
        logger.error(f"Unable to load data: {error}")
        sys.exit(1)
   
    df_before = df.copy()

    try:
        df = process_data(df, config)
    except ValueError as error:
        logger.error(f"Unable to process data: {error}")
        sys.exit(1)

    report = create_cleaning_report(df_before, df)
    print(report)

    logger.info(f"Processing complete: {report}")

    df.to_csv(args.output, index=False)

    logger.info(f"Cleaned data saved to: {args.output}")
if __name__ == "__main__":
    main()