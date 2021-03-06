For Data Collection, from TD Ameritrade, you need to have two accounts:
- TD Ameritrade Developer's Account
- TD Ameritrade Brokerage Account.

Follow the below steps:
1. In config.py (sample_config.py) update the 
- TD Ameritrade details
  - token path - just specify the path in current working directory where
     the generated token will be stored
  - chrome driver path - where chromedriver is stored.
  - api_key, redirect_uri - Get these details from TD AMeritrade Developer's Account.
  - account_id - Get this detail from TD Ameritrade Brokerage Account.
- Timescale DB details
- ticker_path - where input ticker csv file is stored.

5. Sample Tickers(nasdaq101-103.csv) are attached in 'nasdaqtickerlist'
6. Run streamingdatatodb.py, 
   to store the incoming JSON to DB.