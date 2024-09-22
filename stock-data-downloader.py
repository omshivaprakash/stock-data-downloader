import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def download_stock_data(ticker, start_date, end_date, output_file):
    # Download the data
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    
    # Save to CSV
    df.to_csv(output_file)
    print(f"Data saved to {output_file}")

# Example usage
ticker = "NTPC.NS"  # .NS suffix for NSE stocks
end_date = datetime.now()
start_date = end_date - timedelta(days=365)  # Last 1 year of data

output_file = f"{ticker}_historical_data.csv"

download_stock_data(ticker, start_date, end_date, output_file)

# To use for other companies, simply change the ticker
# For example, for Reliance Industries:
# ticker = "RELIANCE.NS"
# download_stock_data(ticker, start_date, end_date, f"{ticker}_historical_data.csv")
