from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from stocks import *

# Base = declarative_base()


class Connection:

    def __init__(self, db_path='sqlite:///stock_data.db'):
        self.engine = create_engine(db_path)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def insert_or_update(self, data_list, model_class, unique_keys=("Ticker", "Date")):
        """Generic insert or update function for any table."""
        session = self.Session()
        for data in data_list:
            print(data)
            try:
                entry = model_class(**data)
                session.add(entry)
                session.commit()
            except IntegrityError:
                session.rollback()
                query = session.query(model_class)
                for key in unique_keys:
                    if key in data:
                        query = query.filter_by(**{key: data[key]})
                entry_to_update = query.first()
                if entry_to_update:
                    for key, value in data.items():
                        setattr(entry_to_update, key, value)
                    session.commit()
        session.close()

    def insert_company_info(self, company_info):
        """Insert or update company information."""
        session = self.Session()
        try:
            company_entry = Stocks(**company_info)
            session.add(company_entry)
            session.commit()
        except IntegrityError:
            # If the unique constraint is violated, we update
            session.rollback()  # Rollback the failed insert
            company_to_update = session.query(Stocks).filter_by(Ticker=company_info['Ticker']).first()
            if company_to_update:
                for key, value in company_info.items():
                    setattr(company_to_update, key, value)
                session.commit()
        finally:
            session.close()

    def insert_stock_data_daily(self, stock_data_list):
        """Insert daily stock data."""
        self.insert_or_update(stock_data_list, StockData)

    def insert_stock_data_5min(self, stock_data_list):
        """Insert 5min stock data."""
        self.insert_or_update(stock_data_list, StockData5Min)

    def insert_stock_data_15min(self, stock_data_list):
        """Insert 15min stock data."""
        self.insert_or_update(stock_data_list, StockData15Min)

    def insert_stock_data_30min(self, stock_data_list):
        """Insert 30min stock data."""
        self.insert_or_update(stock_data_list, StockData30Min)

    def insert_stock_data_60min(self, stock_data_list):
        """Insert 60min stock data."""
        self.insert_or_update(stock_data_list, StockData60Min)

    def insert_stock_data_weekly(self, stock_data_list):
        """Insert weekly stock data."""
        self.insert_or_update(stock_data_list, StockDataWeekly)

    def insert_stock_data_monthly(self, stock_data_list):
        """Insert monthly stock data."""
        self.insert_or_update(stock_data_list, StockDataMonthly)

    def insert_stock_data_quarterly(self, stock_data_list):
        """Insert quarterly stock data."""
        self.insert_or_update(stock_data_list, StockDataQuarterly)

    def insert_stock_data_yearly(self, stock_data_list):
        """Insert yearly stock data."""
        self.insert_or_update(stock_data_list, StockDataYearly)

    def insert_news_events(self, news_list):
        """Insert news events."""
        with self.Session() as session:
            for news in news_list:
                news_entry = NewsEvents(**news)
                session.add(news_entry)
            session.commit()

    def insert_dividends(self, dividends_list):
        """Insert dividends data."""
        with self.Session() as session:
            for dividend in dividends_list:
                try:
                    dividend_entry = Dividends(**dividend)
                    session.add(dividend_entry)
                except TypeError as e:
                    # Better error handling: print the error and the problematic data
                    print(f"Failed to unpack data: {dividend}. Error: {e}")
            session.commit()

    def insert_splits(self, splits_list):
        """Insert stock splits data."""
        with self.Session() as session:
            for split in splits_list:
                try:
                    split_entry = Splits(**split)
                    session.add(split_entry)
                except TypeError as e:
                    # Better error handling: print the error and the problematic data
                    print(f"Failed to unpack data: {split}. Error: {e}")
            session.commit()

    def insert_fundamental_data(self, fundamental_data_list):
        """Insert fundamental data."""
        with self.Session() as session:
            for data in fundamental_data_list:
                fundamental_data_entry = FundamentalData(**data)
                session.add(fundamental_data_entry)
            session.commit()

    def insert_stock_data_daily_adjusted(self, stock_data_list):
        """Insert daily adjusted stock data."""
        self.insert_or_update(stock_data_list, StockDataDailyAdjusted)

    def insert_stock_data_weekly_adjusted(self, stock_data_list):
        """Insert weekly adjusted stock data."""
        self.insert_or_update(stock_data_list, StockDataWeeklyAdjusted)

    def insert_stock_data_monthly_adjusted(self, stock_data_list):
        """Insert monthly adjusted stock data."""
        self.insert_or_update(stock_data_list, StockDataMonthlyAdjusted)

    def insert_stock_data_quarterly_adjusted(self, stock_data_list):
        """Insert quarterly adjusted stock data."""
        self.insert_or_update(stock_data_list, StockDataQuarterlyAdjusted)

    def insert_stock_data_yearly_adjusted(self, stock_data_list):
        """Insert yearly adjusted stock data."""
        self.insert_or_update(stock_data_list, StockDataYearlyAdjusted)

    def insert_stock_data_5min_adjusted(self, stock_data_list):
        """Insert 5min adjusted stock data."""
        self.insert_or_update(stock_data_list, StockDataDaily5MinAdjusted)

    def insert_stock_data_15min_adjusted(self, stock_data_list):
        """Insert 15min adjusted stock data."""
        self.insert_or_update(stock_data_list, StockDataDaily15MinAdjusted)

    def insert_stock_data_30min_adjusted(self, stock_data_list):
        """Insert 30min adjusted stock data."""
        self.insert_or_update(stock_data_list, StockDataDaily30MinAdjusted)

    def insert_stock_data_60min_adjusted(self, stock_data_list):
        """Insert 60min adjusted stock data."""
        self.insert_or_update(stock_data_list, StockDataDaily60MinAdjusted)


if __name__ == '__main__':
    db = Connection()

    # Insert stock info for Apple
    apple_info = {
        'Ticker': 'AAPL',
        'CompanyName': 'Apple Inc.',
        'Sector': 'Technology',
        'Industry': 'Consumer Electronics'
    }
    db.insert_stock_info(apple_info)

    # Insert some sample stock data for Apple
    sample_data = [
        {
            'Date': '2023-10-20',
            'Ticker': 'AAPL',
            'Open': 150.0,
            'High': 155.0,
            'Low': 148.0,
            'Close': 154.0,
            'AdjClose': 154.0,
            'Volume': 1000000
        }
    ]
    db.insert_stock_data(sample_data)
