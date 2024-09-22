import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def download_stock_data(ticker, start_date, end_date, output_file):
    # Download the data
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    
    # Save to CSV
    df.to_csv(output_file)
    print(f"Data saved to {output_file}")
    
    return df

def create_stock_chart(df, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'])
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.grid(True)
    
    # Rotate and align the tick labels so they look better
    plt.gcf().autofmt_xdate()
    
    # Save the chart
    chart_file = f"{ticker}_stock_chart.png"
    plt.savefig(chart_file)
    print(f"Chart saved to {chart_file}")
    
    # Show the chart (optional, comment out if running on a server without display)
    plt.show()

# Example usage
ticker = "NTPC.NS"  # .NS suffix for NSE stocks
end_date = datetime.now()
start_date = end_date - timedelta(days=365)  # Last 1 year of data

output_file = f"{ticker}_historical_data.csv"

# Download data
df = download_stock_data(ticker, start_date, end_date, output_file)

# Create and save chart
create_stock_chart(df, ticker)

# To use for other companies, simply change the ticker
# For example, for Reliance Industries:
# ticker = "RELIANCE.NS"
# df = download_stock_data(ticker, start_date, end_date, f"{ticker}_historical_data.csv")
# create_stock_chart(df, ticker)
