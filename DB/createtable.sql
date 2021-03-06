CREATE TABLE stocksdata(time TIMESTAMPTZ DEFAULT Now(),
            timestamp bigint NOT NULL,
            key TEXT NOT NULL,
            DELAYED BOOLEAN,
            BID_PRICE FLOAT,
            ASK_PRICE FLOAT,
            LAST_PRICE FLOAT,
            BID_SIZE FLOAT,
            ASK_SIZE FLOAT,
            ASK_ID CHAR,
            BID_ID CHAR,
            TOTAL_VOLUME BIGINT,
            LAST_SIZE FLOAT,
            TRADE_TIME INT,
            QUOTE_TIME INT,
            HIGH_PRICE FLOAT,
            LOW_PRICE FLOAT,
            BID_TICK CHAR,
            CLOSE_PRICE FLOAT,
            EXCHANGE_ID CHAR,
            MARGINABLE BOOLEAN,
            SHORTABLE BOOLEAN,
            ISLAND_BID_DEPRECATED FLOAT,
            ISLAND_ASK_DEPRECATED FLOAT,
            ISLAND_VOLUME_DEPRECATED FLOAT,
            QUOTE_DAY INT,
            TRADE_DAY INT,
            VOLATILITY FLOAT,
            DESCRIPTION TEXT,
            LAST_ID CHAR,
            DIGITS INT,
            OPEN_PRICE FLOAT,
            NET_CHANGE FLOAT,
            HIGH_52_WEEK FLOAT,
            LOW_52_WEEK FLOAT,
            PE_RATIO FLOAT,
            DIVIDEND_AMOUNT FLOAT,
            DIVIDEND_YIELD FLOAT,
            ISLAND_BID_SIZE_DEPRECATED INT,
            ISLAND_ASK_SIZE_DEPRECATED INT,
            NAV FLOAT,
            FUND_PRICE FLOAT,
            EXCHANGE_NAME TEXT,
            DIVIDEND_DATE TEXT,
            IS_REGULAR_MARKET_QUOTE BOOLEAN,
            IS_REGULAR_MARKET_TRADE BOOLEAN,
            REGULAR_MARKET_LAST_PRICE FLOAT,
            REGULAR_MARKET_LAST_SIZE FLOAT,
            REGULAR_MARKET_TRADE_TIME int,
            REGULAR_MARKET_TRADE_DAY INT,
            REGULAR_MARKET_NET_CHANGE FLOAT,
            SECURITY_STATUS TEXT,
             MARK DOUBLE PRECISION,
             QUOTE_TIME_IN_LONG BIGINT,
            TRADE_TIME_IN_LONG BIGINT,
            REGULAR_MARKET_TRADE_TIME_IN_LONG BIGINT
);
