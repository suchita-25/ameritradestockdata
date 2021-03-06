import asyncio
import psycopg2
from tda.auth import easy_client
from tda.streaming import StreamClient
import pandas as pd
import config

CONN = psycopg2.connect(host=config.DB_HOST,
                        database=config.DB_NAME,
                        user=config.DB_USER,
                        password=config.DB_PASS)

cursor = CONN.cursor()

CLIENT = easy_client(
    api_key=config.api_key,
    redirect_uri=config.redirect_uri,
    token_path=config.token_path)

STREAM_CLIENT = StreamClient(client, account_id=config.account_id)


def order_book_handler(msg):


    count = len(msg['content'])
    CONN.commit()
    try:
        for i in range(count):
            dict2 = {**msg['content'][i]}
            print(dict2)
            cols = dict2.keys()
            cols_str = ','.join(cols)
            vals = [dict2[k] for k in cols]
            print("Vals", vals)
            vals_str = ','.join(["%s" for j in range(len(vals))])
            sql_str = """INSERT INTO stocksdata({0},{1}) VALUES ({2}, {3})""" \
                .format('timestamp', cols_str, msg['timestamp'], vals_str)
            print(sql_str)
            cursor.execute(sql_str, vals)
    except:
        print('Halted')
        CONN.commit()


CONN.commit()

async def read_stream():
    await STREAM_CLIENT.login()
    await STREAM_CLIENT.quality_of_service(StreamClient.QOSLevel.EXPRESS)

    # Always add handlers before subscribing because many streams start sending
    # data immediately after success, and messages with no handlers are dropped.
    # stream_client.add_nasdaq_book_handler(
    #         lambda msg: print(json.dumps(msg, indent=4)))
    # await stream_client.nasdaq_book_subs(['GOOG']) #Nasdaq
    #  await stream_client.listed_book_subs(['GOOG']) #NYSE Bid & ASk
    ftp1 = pd.read_csv(config.ticker_path, usecols=['Symbol'])
    list1 = ftp1.Symbol.to_list()
    print(list1)

    await STREAM_CLIENT.level_one_equity_subs(list1)
    STREAM_CLIENT.add_level_one_equity_handler(order_book_handler)
    # stream_client.add_listed_book_handler(order_book_handler)
    while True:
        await STREAM_CLIENT.handle_message()
asyncio.run(read_stream())

# async def main():
#     print('Started, press ctrl+C')
#     asyncio.run(read_stream())
#
# if __name__ == '__main__':
#
#     async def close():
#         print('Finalizing...')
#         await asyncio.sleep(1)
#
#         loop = asyncio.get_event_loop()
#         try:
#             loop.run_until_complete(main())
#         except KeyboardInterrupt:
#             loop.run_until_complete(close())
#         finally:
#             print('Program finished')#