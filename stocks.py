from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, UniqueConstraint, Sequence
from sqlalchemy.orm import relationship

Base = declarative_base()


class Stocks(Base):
    __tablename__ = 'Stocks'
    Ticker = Column(String, primary_key=True)
    CompanyName = Column(String)
    Sector = Column(String)
    Industry = Column(String)

    _5min_data = relationship('StockData5Min', back_populates='stock')
    _15min_data = relationship('StockData15Min', back_populates='stock')
    _30min_data = relationship('StockData30Min', back_populates='stock')
    _60min_data = relationship('StockData60Min', back_populates='stock')
    daily_data = relationship('StockDataDaily', back_populates='stock')
    weekly_data = relationship('StockDataWeekly', back_populates='stock')
    monthly_data = relationship('StockDataMonthly', back_populates='stock')
    quarterly_data = relationship('StockDataQuarterly', back_populates='stock')
    yearly_data = relationship('StockDataYearly', back_populates='stock')

    _5min_adjusted_data = relationship('StockDataDaily5MinAdjusted', back_populates='stock')
    _15min_adjusted_data = relationship('StockDataDaily15MinAdjusted', back_populates='stock')
    _30min_adjusted_data = relationship('StockDataDaily30MinAdjusted', back_populates='stock')
    _60min_adjusted_data = relationship('StockDataDaily60MinAdjusted', back_populates='stock')
    daily_adjusted_data = relationship('StockDataDailyAdjusted', back_populates='stock')
    weekly_adjusted_data = relationship('StockDataWeeklyAdjusted', back_populates='stock')
    monthly_adjusted_data = relationship('StockDataMonthlyAdjusted', back_populates='stock')
    quarterly_adjusted_data = relationship('StockDataQuarterlyAdjusted', back_populates='stock')
    yearly_adjusted_data = relationship('StockDataYearlyAdjusted', back_populates='stock')

    dividends = relationship('Dividends', back_populates='stock')
    splits = relationship('Splits', back_populates='stock')
    fundamentals = relationship('FundamentalData', back_populates='stock')


class StockData(Base):
    __tablename__ = 'StockData'

    # NOTE: for usage with other databases, you should prefer Sequence over autoincrement=True
    # ID = Column(Integer, Sequence('stock_data_yearly_id_seq'), primary_key=True)
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    AdjClose = Column(Float)
    Volume = Column(Integer)
    __table_args__ = (UniqueConstraint('Date', 'Ticker'), )


class StockData5Min(Base):
    __tablename__ = 'StockData5Min'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    Volume = Column(Integer)

    stock = relationship("Stocks", back_populates="_5min_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'), )


class StockData15Min(Base):
    __tablename__ = 'StockData15Min'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    Volume = Column(Integer)

    stock = relationship("Stocks", back_populates="_15min_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'), )


class StockData30Min(Base):
    __tablename__ = 'StockData30Min'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    Volume = Column(Integer)

    stock = relationship("Stocks", back_populates="_30min_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'), )


class StockData60Min(Base):
    __tablename__ = 'StockData60Min'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    Volume = Column(Integer)

    stock = relationship("Stocks", back_populates="_60min_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'), )


class StockDataDaily(Base):
    __tablename__ = 'StockDataDaily'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    Volume = Column(Integer)

    stock = relationship("Stocks", back_populates="daily_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'), )


class StockDataWeekly(Base):
    __tablename__ = 'StockDataWeekly'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    Volume = Column(Integer)

    stock = relationship("Stocks", back_populates="weekly_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'), )


class StockDataMonthly(Base):
    __tablename__ = 'StockDataMonthly'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    Volume = Column(Integer)

    stock = relationship("Stocks", back_populates="monthly_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'), )


class StockDataQuarterly(Base):
    __tablename__ = 'StockDataQuarterly'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    AdjustedClose = Column(Float)
    Volume = Column(Integer)

    stock = relationship("Stocks", back_populates="quarterly_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'),)


class StockDataYearly(Base):
    __tablename__ = 'StockDataYearly'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    AdjustedClose = Column(Float)
    Volume = Column(Integer)

    stock = relationship("Stocks", back_populates="yearly_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'),)


class StockDataDaily5MinAdjusted(Base):
    __tablename__ = 'StockDataDaily5MinAdjusted'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    AdjustedClose = Column(Float)
    Volume = Column(Integer)
    DividendAmount = Column(Float)
    SplitRatio = Column(String)

    stock = relationship("Stocks", back_populates="_5min_adjusted_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'),)


class StockDataDaily15MinAdjusted(Base):
    __tablename__ = 'StockDataDaily15MinAdjusted'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    AdjustedClose = Column(Float)
    Volume = Column(Integer)
    DividendAmount = Column(Float)
    SplitRatio = Column(String)

    stock = relationship("Stocks", back_populates="_15min_adjusted_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'),)


class StockDataDaily30MinAdjusted(Base):
    __tablename__ = 'StockDataDaily30MinAdjusted'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    AdjustedClose = Column(Float)
    Volume = Column(Integer)
    DividendAmount = Column(Float)
    SplitRatio = Column(String)

    stock = relationship("Stocks", back_populates="_30min_adjusted_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'),)


class StockDataDaily60MinAdjusted(Base):
    __tablename__ = 'StockDataDaily60MinAdjusted'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    AdjustedClose = Column(Float)
    Volume = Column(Integer)
    DividendAmount = Column(Float)
    SplitRatio = Column(String)

    stock = relationship("Stocks", back_populates="_60min_adjusted_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'),)


class StockDataDailyAdjusted(Base):
    __tablename__ = 'StockDataDailyAdjusted'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    AdjustedClose = Column(Float)
    Volume = Column(Integer)
    DividendAmount = Column(Float)
    SplitRatio = Column(String)

    stock = relationship("Stocks", back_populates="daily_adjusted_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'),)


class StockDataWeeklyAdjusted(Base):
    __tablename__ = 'StockDataWeeklyAdjusted'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    AdjustedClose = Column(Float)
    Volume = Column(Integer)
    DividendAmount = Column(Float)
    SplitRatio = Column(String)

    stock = relationship("Stocks", back_populates="weekly_adjusted_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'),)


class StockDataMonthlyAdjusted(Base):
    __tablename__ = 'StockDataMonthlyAdjusted'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    AdjustedClose = Column(Float)
    Volume = Column(Integer)
    DividendAmount = Column(Float)
    SplitRatio = Column(String)

    stock = relationship("Stocks", back_populates="monthly_adjusted_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'),)


class StockDataQuarterlyAdjusted(Base):
    __tablename__ = 'StockDataQuarterlyAdjusted'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    AdjustedClose = Column(Float)
    Volume = Column(Integer)
    DividendAmount = Column(Float)
    SplitRatio = Column(String)

    stock = relationship("Stocks", back_populates="quarterly_adjusted_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'),)


class StockDataYearlyAdjusted(Base):
    __tablename__ = 'StockDataYearlyAdjusted'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    AdjustedClose = Column(Float)
    Volume = Column(Integer)
    DividendAmount = Column(Float)
    SplitRatio = Column(String)

    stock = relationship("Stocks", back_populates="yearly_adjusted_data")

    __table_args__ = (UniqueConstraint('Date', 'Ticker'),)


class NewsEvents(Base):
    __tablename__ = 'NewsEvents'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    EventDescription = Column(String)
    __table_args__ = (UniqueConstraint('Date', 'Ticker'), )


class Dividends(Base):
    __tablename__ = 'Dividends'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    DividendAmount = Column(Float)

    stock = relationship('Stocks', back_populates='dividends')

    __table_args__ = (UniqueConstraint('Date', 'Ticker'), )


class Splits(Base):
    __tablename__ = 'Splits'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    SplitRatio = Column(String)

    stock = relationship('Stocks', back_populates='splits')

    __table_args__ = (UniqueConstraint('Date', 'Ticker'), )


class FundamentalData(Base):
    __tablename__ = 'FundamentalData'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date, nullable=False)
    Ticker = Column(String, ForeignKey('Stocks.Ticker'), nullable=False)
    EPS = Column(Float)
    Revenue = Column(Float)
    Profit = Column(Float)

    stock = relationship('Stocks', back_populates='fundamentals')

    __table_args__ = (UniqueConstraint('Date', 'Ticker'), )
