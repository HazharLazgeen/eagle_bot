from binance_client import client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
from tickers import pairs
import time
from alive_progress import alive_bar

kline_volues = {}


def streaming_data_process(msg):

	"""
	{
				"e": "kline",					# event type
                "E": 1499404907056,				# event time
                "s": "ETHBTC",					# symbol
                "k": {
                    "t": 1499404860000, 		# start time of this bar
                    "T": 1499404919999, 		# end time of this bar
                    "s": "ETHBTC",				# symbol
                    "i": "1m",					# interval
                    "f": 77462,					# first trade id
                    "L": 77465,					# last trade id
                    "o": "0.10278577",			# open
                    "c": "0.10278645",			# close
                    "h": "0.10278712",			# high
                    "l": "0.10278518",			# low
                    "v": "17.47929838",			# volume
                    "n": 4,						# number of trades
                    "x": false,					# whether this bar is final
                    "q": "1.79662878",			# quote volume
                    "V": "2.34879839",			# volume of active buy
                    "Q": "0.24142166",			# quote volume of active buy
                    "B": "13279784.01349473"	# can be ignored
			}
	"""
	# 0 = best_buy_price, 1 = best_sell_price
	kline_volues[msg['s']]=[float(msg['k']["c"]), float(msg['k']["q"])]


bm = BinanceSocketManager(client)
print("start init streaming ...")
print("You can't stop the program until it has finished initializing \n")
for pair in pairs:
	conn_key = bm.start_kline_socket(pair, streaming_data_process,interval=client.KLINE_INTERVAL_1DAY)

bm.start()
with alive_bar(len(pairs)) as bar:  # or a 1000 in the loop example.
    for i in range(len(pairs)):
        time.sleep(15/len(pairs))
        bar()
print("\nend init streaming ....")

"""while True:
    print(kline_volues["BTCUSDT"])"""