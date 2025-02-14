# Stock Data Processor

## Overview
This Python script processes stock trading data from a CSV file, extracting key financial metrics such as total trade volume, the largest single trade, and closing prices. Designed for speed and accuracy, it operates without third-party libraries, making it suitable for large datasets.

## Performance (Time & Space Complexity)
**Time Complexity**
- This script processes stock trading data in O(N) time complexity, where N is the number of trades.

**Space Complexity**
- The space complexity is O(K) + O(H), where K is the number of unique companies and H is the number of trading hours, making it scalable without excessive memory usage.

## Features
- **Efficient CSV parsing:** Reads data line by line to optimize memory usage.
- **Incremental aggregation:**
  - Identifies the highest-volume company.
  - Determines the lowest-dollar-volume company.
  - Finds the largest single trade (price × volume).
  - Pinpoints the hour with the lowest trade volume.
  - Captures closing prices for all stocks.

## How It Works
1. Reads stock trading data line by line from a CSV file.
2. Aggregates metrics using dictionaries for efficient calculations.
3. Computes and returns a tuple containing:
   - Company with the highest total share volume.
   - Average share volume per trade.
   - Largest single trade value.
   - Hour with the lowest trading volume.
   - Total shares and dollar volume traded.
   - Total number of unique companies.
   - Company with the lowest total dollar volume.
   - Closing price of each stock.

## Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/stock-data-processor.git
   cd stock-data-processor
