# program to write top 1800 traded on a csv file. SQL dump to CSV.
import csv
import psycopg2
import config

CONN = psycopg2.connect(host=config.DB_HOST,
                        database=config.DB_NAME,
                        user=config.DB_USER,
                        password=config.DB_PASS)

print("Database opened successfully")
CURSOR = CONN.cursor()

# TOP 10 stocks traded on March 5th
SQL1 = "select key, count(*),sum(total_volume) from stocksdata where date(time)='2021-03-29' group by key, total_volume order by total_volume DESC limit 1800;"
SQL2 = "select key, count(*) from stocksdata where date(time)='2021-03-05' group by key order by count(*) ASC limit 10;"
SQL3 = "select timestamp,time, last_price from stocksdata where date(time)>'2021-03-26' and key = 'SNDL' and last_price is NOT NULL;"
SQL4 = "select time, key, last_price from stocksdata where date(time) >'2021-03-27' and key in ('FB', 'AAPL', 'NFLX', 'GOOG', 'MSFT') group by key and last_price is NOT NULL"
CURSOR.execute(SQL3)
result = CURSOR.fetchall()

fp = open('sndl.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(result)
fp.close()
