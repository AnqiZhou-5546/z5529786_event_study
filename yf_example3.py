"""yf_example3.py
Download Qantas stock prices for a given year into a CSV file.
"""
import os
import yf_example2
import toolkit_config as cfg


def qan_prc_to_csv(year):
    """
    Args:
        year (int): The year for which to download the data.

    Purpose:
        This function uses yf_example2.yf_prc_to_csv to download Qantas stock prices
        from January 1 to December 31 of the specified year. The data is saved in
        a CSV file named qan_prc_YYYY.csv in the data folder.
    """
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"

    filename = f"qan_prc_{year}.csv"
    Path = os.path.join(cfg.DATADIR, filename)
    yf_example2.yf_prc_to_csv(start=start_date, end=end_date, tic='QAN.AX', pth=Path)

    print(f"Data downloaded and saved to: {Path}")


if __name__ == "__main__":
    # Test case: Download Qantas stock prices for year 2020
    qan_prc_to_csv(year=2020)
