CREATE TABLE Stocks (
    Ticker TEXT PRIMARY KEY,
    CompanyName TEXT,
    Sector TEXT,
    Industry TEXT
);

CREATE TABLE StockData (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    AdjClose REAL,
    Volume INTEGER,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockData5Min (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    Volume INTEGER,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockData15Min (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    Volume INTEGER,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockData30Min (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    Volume INTEGER,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockData60Min (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    Volume INTEGER,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockDataDaily (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    AdjClose REAL,
    Volume INTEGER,
    UNIQUE(Date, Ticker)
);


CREATE TABLE StockDataWeekly (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    AdjClose REAL,
    Volume INTEGER,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockDataMonthly (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    AdjClose REAL,
    Volume INTEGER,
    UNIQUE(Date, Ticker)
);


CREATE TABLE StockDataQuarterly (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    AdjustedClose REAL,
    Volume INTEGER,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockDataYearly (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    AdjustedClose REAL,
    Volume INTEGER,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockDataDaily5MinAdjusted (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    AdjustedClose REAL,
    Volume INTEGER,
    DividendAmount REAL,
    SplitRatio TEXT,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockDataDaily15MinAdjusted (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    AdjustedClose REAL,
    Volume INTEGER,
    DividendAmount REAL,
    SplitRatio TEXT,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockDataDaily30MinAdjusted (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    AdjustedClose REAL,
    Volume INTEGER,
    DividendAmount REAL,
    SplitRatio TEXT,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockDataDaily60MinAdjusted (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    AdjustedClose REAL,
    Volume INTEGER,
    DividendAmount REAL,
    SplitRatio TEXT,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockDataDailyAdjusted (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    AdjustedClose REAL,
    Volume INTEGER,
    DividendAmount REAL,
    SplitRatio TEXT,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockDataWeeklyAdjusted (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    AdjustedClose REAL,
    Volume INTEGER,
    DividendAmount REAL,
    SplitRatio TEXT,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockDataMonthlyAdjusted (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    AdjustedClose REAL,
    Volume INTEGER,
    DividendAmount REAL,
    SplitRatio TEXT,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockDataQuarterlyAdjusted (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    AdjustedClose REAL,
    Volume INTEGER,
    DividendAmount REAL,
    SplitRatio TEXT,
    UNIQUE(Date, Ticker)
);

CREATE TABLE StockDataYearlyAdjusted (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    AdjustedClose REAL,
    Volume INTEGER,
    DividendAmount REAL,
    SplitRatio TEXT,
    UNIQUE(Date, Ticker)
);

CREATE TABLE NewsEvents (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    EventDescription TEXT,
    UNIQUE(Date, Ticker)
);

CREATE TABLE Dividends (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    DividendAmount REAL,
    UNIQUE(Date, Ticker)
);

CREATE TABLE Splits (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    SplitRatio TEXT,
    UNIQUE(Date, Ticker)
);

CREATE TABLE FundamentalData (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date DATE NOT NULL,
    Ticker TEXT NOT NULL REFERENCES Stocks(Ticker),
    EPS REAL,
    Revenue REAL,
    Profit REAL,
    -- Add other metrics as needed
    UNIQUE(Date, Ticker)
);

