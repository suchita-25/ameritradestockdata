# run sql query
import psycopg2
import config

CONN = psycopg2.connect(host=config.DB_HOST,
                        database=config.DB_NAME,
                        user=config.DB_USER,
                        password=config.DB_PASS)

print("Database opened successfully")
CURSOR = CONN.cursor()

SQL1 = "select last_price from stocksdata where key='MSFT' and date(time)='2021-03-05'and last_price is NOT NULL"
SQL2 = "select last_price from stocksdata where key='MRNA' and date(time)='2021-03-05'and last_price is NOT NULL"
SQL3 = "select key,last_price, time from stocksdata where date(time)='2021-03-29' and key in ('GOOG','MRNA')"
SQL5="SELECT time,key, open_price,close_price,low_price,high_price FROM stocksdata WHERE key in ('FB', 'GOOG','MSFT') and date(time)>'2021-03-05' order by date(time),key;"
CURSOR.execute(SQL5)
result2 = CURSOR.fetchall()
print(result2)