# Function: process_stock_data
# This function processes stock trading data and returns a tuple of length 8, containing:
# 
# 1. The company with the highest total share volume traded.
#    - Which comapany had the most shares traded in total.
# 2. The average share volume traded.
#    - On average, how many shares were traded per trade
# 3. The largest ($$$) single trade made.
#    - What is the most expensive trade
#    - A single trade's value is price * volume
# 4. The hour with the lowest volume of trades.
#    - Which hour (e.g., 10, 11, 12, etc.) had the fewst shares traded?
# 5. Total share and dollar volume traded over the day.
#    - How many total shares and total dollar were traded
# 6. Total number of companies in the dataset.
#    - How many unique tickets are there?
# 7. The company with the lowest dollar volume traded.
#    - Which company had the lowest total trade value (price * volume)
# 8. The closing price of each company’s stock.
#    - What was the last tradeded price for each company
#
# Constraints:
# - Function Written in Python
# - No third-party libraries like pandas or numpy are used.
# - The input data is expected to be a list of dictionaries with relevant trade details.

# Data:
# Timestamp: When the trade happened.
# Ticker: The company (e.g., AAPL for Apple).
# Price: The price per share.
# Volume: How many shares were traded.

def process_stock_data(file_path):

    # Initialize dictionaries to store aggregated values
    # Track total shares traded per company
    company_shares = {} # {'AAL': 500, 'GOOG': 400}

    # Track total dollar volume per company (price * volume)
    company_dollars = {} # {'AAPL': 7500, 'GOOG': 50000}

    # Track total shares traded per hour
    hourly_volume = {} # {'10': 1000, '11': 1500}
    
    # Store the last traded price for each company
    closing_prices = {} # {'AAPL': 155.0, 'GOOG': 2850.0}
    
    # Track total shares, total dollars, and largest trade
    # Track total shares traded
    total_shares = 0
    # Track total money traded
    total_dollars = 0
    max_trade_value = 0 # Most expensive trade (price * volume)

    # Open the CSV file and read the data
    with open(file_path, 'r') as file:
        next(file)  # Skip header row
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 4:
                continue  # Skip invalid lines
            
            timestamp, ticker, price, volume = parts
            price = float(price)
            volume = int(volume)
            trade_value = price * volume
            hour = timestamp.split(' ')[-1].split(':')[0] # Extract hour from timestamp

            # Track total shares and dollar volume
            total_shares += volume
            total_dollars += trade_value

            # Track pre-company shares & dollar value
            company_shares[ticker] = company_shares.get(ticker, 0) + volume
            company_dollars[ticker] = company_dollars.get(ticker, 0) + trade_value

            # Track the largest single trade
            max_trade_value = max(max_trade_value, trade_value)

            # Track pre-hour volume
            hourly_volume[hour] = hourly_volume.get(hour, 0) + volume

            # Track last known price
            closing_prices[ticker] = price

    # Computing Final Results
    highest_volume_company = max(company_shares, key=company_shares.get)
    lowest_dollar_volume_company = min(company_dollars, key=company_dollars.get)
    avg_share_volume = total_shares / len(company_shares) # (Sum of all values) / (Total number of values). 
    lowest_trade_hour = min(hourly_volume, key=hourly_volume.get)
    total_companies = len(company_shares)

    return (
        highest_volume_company,   # 1
        avg_share_volume,         # 2
        max_trade_value,          # 3
        lowest_trade_hour,        # 4
        total_shares,             # 5
        total_dollars,            # 6
        total_companies,          # 7
        lowest_dollar_volume_company,  # 8
        closing_prices            # 9 - Dictionary of closing prices
    )

# Example usage:
file_path = "ticker_data.csv"  # Ensure the file is in the same directory or provide the full path
result = process_stock_data(file_path)
print(result)
