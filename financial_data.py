import yfinance as yf


class FinancialData:

    def __init__(self, ticker_symbol):
        self.ticker = yf.Ticker(ticker_symbol)

    def get_company_info(self):
        """Get company information like name, sector, and industry."""
        info = self.ticker.info
        return {
            'Ticker': info.get('symbol', None),
            'CompanyName': info.get('longName', None),
            'Sector': info.get('sector', None),
            'Industry': info.get('industry', None)
        }

    def get_historical_data(self, period="1y", interval="1d"):
        """Get historical stock data based on the specified period and interval."""
        data = self.ticker.history(period=period, interval=interval)
        return data.reset_index().to_dict(orient='records')

    def get_dividends(self):
        """Get dividend data."""
        actions = self.ticker.actions
        dividends = actions[actions['Dividends'] != 0]
        return dividends.reset_index().to_dict(orient='records')

    def get_splits(self):
        """Get stock splits data."""
        actions = self.ticker.actions
        splits = actions[actions['Stock Splits'] != 0]
        return splits.reset_index().to_dict(orient='records')

    def get_eps(self):
        """Get Earnings Per Share. Note: This provides the latest EPS, not historical."""
        return self.ticker.info.get('trailingEps', None)

    def transform_historical_data(self, data, interval="1d"):
        """Transform historical data based on the specified interval."""
        transformed_data = []

        for record in data:
            entry = {
                'Date': record['Date'].date(),
                'Ticker': self.ticker.ticker,
                'Open': record['Open'],
                'High': record['High'],
                'Low': record['Low'],
                'Close': record['Close'],
                'Volume': record['Volume']
            }

            if 'Dividends' in record:
                entry['DividendAmount'] = record['Dividends']

            if 'Stock Splits' in record:
                entry['SplitRatio'] = str(record['Stock Splits'])

            if interval in ["1d", "5d"]:
                entry['AdjustedClose'] = record['Close']  # Assuming Close is adjusted. Correct if needed.

            transformed_data.append(entry)

        return transformed_data

    def transform_dividends(self, data):
        """Transform dividend data."""
        return [{
            'Date': record['Date'].date(),
            'Ticker': self.ticker.ticker,
            'DividendAmount': record['Dividends']
        } for record in data]

    def transform_splits(self, data):
        """Transform split data."""
        return [{
            'Date': record['Date'].date(),
            'Ticker': self.ticker.ticker,
            'SplitRatio': str(record['Stock Splits'])
        } for record in data]

    def get_fundamental_data(self):
        """Get fundamental data."""
        info = self.ticker.info
        return {
            'Ticker': self.ticker.ticker,
            'MarketCap': info.get('marketCap', None),
            'EBITDA': info.get('ebitda', None),
            'PEratio': info.get('trailingPE', None),
            'BookValue': info.get('bookValue', None)
        }


if __name__ == "__main__":
    # Create an instance for Apple stock
    apple_data = FinancialData("AAPL")

    # Get company info
    company_info = apple_data.get_company_info()
    print(company_info)

    # Get historical data
    historical_data = apple_data.get_historical_data(period="1mo", interval="1d")
    for day_data in historical_data:
        print(day_data)

    # Get dividends
    dividends = apple_data.get_dividends()
    print(dividends)

    # Get splits
    splits = apple_data.get_splits()
    print(splits)

    # Get EPS
    eps = apple_data.get_eps()
    print(f"EPS: {eps}")
