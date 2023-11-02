from financial_data import FinancialData
from connection import Connection

from config import database_path


class Fetcher:
    def __init__(self, ticker_symbol, db_path=database_path):
        self.ticker = ticker_symbol
        self.fin_data = FinancialData(ticker_symbol)
        self.connection = Connection(db_path)

    def fetch_and_save_company_info(self):
        company_info = self.fin_data.get_company_info()
        self.connection.insert_company_info(company_info)

    def fetch_and_save_historical_data(self, period="1y", interval="1d", adjusted=False):
        hist_data = self.fin_data.get_historical_data(period, interval)

        dividends_data = self.extract_dividends(hist_data)
        splits_data = self.extract_splits(hist_data)
        # print(hist_data)
        _ = [data.pop('Dividends') for data in hist_data if 'Dividends' in data]
        # _ = [data.pop('DividendAmount') for data in hist_data if 'DividendAmount' in data]
        # _ = [data.pop('SplitRatio') for data in hist_data if 'SplitRatio' in data]
        _ = [data.pop('Stock Splits') for data in hist_data if 'Stock Splits' in data]

        if adjusted:
            hist_data = self.fin_data.transform_historical_data(hist_data, interval)
            if interval == "5m":
                self.connection.insert_stock_data_5min_adjusted(hist_data)
            elif interval == "15m":
                self.connection.insert_stock_data_15min_adjusted(hist_data)
            elif interval == "30m":
                self.connection.insert_stock_data_30min_adjusted(hist_data)
            elif interval == "60m":
                self.connection.insert_stock_data_60min_adjusted(hist_data)
            elif interval == "1d":
                self.connection.insert_stock_data_daily_adjusted(hist_data)
            elif interval == "1wk":
                self.connection.insert_stock_data_weekly_adjusted(hist_data)
            elif interval == "1mo":
                self.connection.insert_stock_data_monthly_adjusted(hist_data)
            elif interval == "3mo":
                self.connection.insert_stock_data_quarterly_adjusted(hist_data)
            elif interval == "1y":
                self.connection.insert_stock_data_yearly_adjusted(hist_data)

        else:
            if interval == "1d":
                self.connection.insert_stock_data_daily(hist_data)
            elif interval == "5m":
                self.connection.insert_stock_data_5min(hist_data)
            elif interval == "15m":
                self.connection.insert_stock_data_15min(hist_data)
            elif interval == "30m":
                self.connection.insert_stock_data_30min(hist_data)
            elif interval == "60m":
                self.connection.insert_stock_data_60min(hist_data)
            elif interval == "1wk":
                self.connection.insert_stock_data_weekly(hist_data)
            elif interval == "1mo":
                self.connection.insert_stock_data_monthly(hist_data)
            elif interval == "3mo":
                self.connection.insert_stock_data_quarterly(hist_data)
            elif interval == "1y":
                self.connection.insert_stock_data_yearly(hist_data)

        self.connection.insert_dividends(dividends_data)
        self.connection.insert_splits(splits_data)

    def extract_dividends(self, hist_data):
        dividends_data = []
        for data in hist_data:
            # Check if dividends exist and are non-zero
            if 'Dividends' in data and data['Dividends'] != 0.0:
                dividends_data.append({
                    'Date': data['Date'].to_pydatetime().date(),
                    'Ticker': self.ticker,
                    'DividendAmount': data.pop('Dividends')
                })

        return dividends_data

    def extract_splits(self, hist_data):
        splits_data = []
        if 'Stock Splits' in hist_data and hist_data['Stock Splits'] != 0.0:
            splits_data.append({
                'Date': hist_data['Date'].to_pydatetime().date(),
                'Ticker': self.ticker,
                'SplitRatio': hist_data.pop('Stock Splits')
            })
        return splits_data

    def fetch_and_save_dividends(self):
        dividends = self.fin_data.get_dividends()
        self.connection.insert_dividends(dividends)

    def fetch_and_save_splits(self):
        splits = self.fin_data.get_splits()
        self.connection.insert_splits(splits)

    def fetch_and_save_fundamental_data(self):
        fundamental_data = self.fin_data.get_eps()
        # Assuming the EPS is just a single value, you might need to wrap it in a list or adjust for structure
        self.connection.insert_fundamental_data([{'EPS': fundamental_data}])

    def fetch_and_save_all(self, period="1y", interval="1d"):
        """Fetch and save all data for convenience."""
        self.fetch_and_save_company_info()
        self.fetch_and_save_historical_data(period, interval)
        self.fetch_and_save_dividends()
        self.fetch_and_save_splits()
        self.fetch_and_save_fundamental_data()


if __name__ == '__main__':
    fetcher = Fetcher("AAPL")
    fetcher.fetch_and_save_all()
