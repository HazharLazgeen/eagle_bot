import time
print("WebSocket Wait 10 Secand")
time.sleep(10)
import json
import websocket
import time
import Eqution as Eq
import Volume_calculator as Vol


def on_open(ws):
    try:
        print("Opened connection WebSocket Start...")
        SUBSCRIBE = {"method": "SUBSCRIBE","params":["!ticker@arr"],"id": 1}
        ws.send(json.dumps(SUBSCRIBE))
    except Exception as massgge:
        #_Send.exaption_error(massgge, "while True Main Bot", "", "")
        print(massgge)
        #time.sleep(10)
        pass


def on_message(ws, message):
    data = json.loads(message)
    date_time, time_stamp , _year, _month, _day, _hour, _minute, _secand = Eq.time_date()
    
    #print(ticker["s"])

    for ticker in data:
        if ((ticker['s'].endswith('USDT') or ticker['s'].endswith('BTC')) and "DOWN" not in ticker['s'] and "UP" not in ticker['s']):
        #if ((ticker['s'].endswith('USDT')) and "DOWN" not in ticker['s'] and "UP" not in ticker['s']):
            Vol.volume_24(ticker['s'],int( ticker['E']), float(ticker['p']), float(ticker['P']), float(ticker['w']), float(ticker['c']), 
                float(ticker['o']), float(ticker['h']), float(ticker['l']), float(ticker['v']), float(ticker['q']), float(ticker['n']),
                float(ticker['Q']), float(ticker['b']), float(ticker['B']), float(ticker['a']), float(ticker['A']),

                date_time, time_stamp , _year, _month, _day, _hour, _minute, _secand
            )

        #save to mongodb


url = "wss://stream.binance.com:9443/ws"
ws = websocket.WebSocketApp(url,on_open=on_open,on_message=on_message)
while True:
    ws.run_forever()  


"""
{
  "e": "24hrTicker",  // Event type
  "E": 123456789,     // Event time
  "s": "BNBBTC",      // Symbol
  "p": "0.0015",      // Price change
  "P": "250.00",      // Price change percent
  "w": "0.0018",      // Weighted average price
  "x": "0.0009",      // First trade(F)-1 price (first trade before the 24hr rolling window)
  "c": "0.0025",      // Last price

  "Q": "10",          // Last quantity
  "b": "0.0024",      // Best bid price
  "B": "10",          // Best bid quantity
  "a": "0.0026",      // Best ask price
  "A": "100",         // Best ask quantity

  "o": "0.0010",      // Open price
  "h": "0.0025",      // High price
  "l": "0.0010",      // Low price
  "v": "10000",       // Total traded base asset volume
  "q": "18",          // Total traded quote asset volume
  "O": 0,             // Statistics open time
  "C": 86400000,      // Statistics close time
  "F": 0,             // First trade ID
  "L": 18150,         // Last trade Id
  "n": 18151          // Total number of trades
}
"""
    