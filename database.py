import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Tredingdb"]
mycol_24hrTicker = db["ticker24h"]











class Types():
    buy_market = "buy_market_orders"
    buy_market_okex = "buy_market_okex"
    sell_market = "sell_market_orders"
    buy_limit = "buy_limit_orders"
    sell_limit = "sell_limit_orders"
    sell_oco = "sell_oco_orders"

class Status():
    def save_status(collection, status, time):
        collection = db[collection]
        data = collection.delete_many({})
        new_stat = {"Status":status, "Time":time}
        data = collection.insert_one(new_stat)
        return data

    def find_status(collection):
        collection = db[collection]
        data = collection.find({})
        for dt in data:
            stat = dt["Status"]
        return stat

class Signals():

    def add(collection, ticker, volume, pct_sl):
        collection = db[collection]
        new_signal = {"Ticker":ticker, "Volume":volume, "SL":pct_sl }
        data = collection.insert_one(new_signal)
        return data

    def find_all(collection):
        tickers = {}
        collection = db[collection]
        data = collection.find({})
        for dt in data:
            tickers[dt["Ticker"]] = [dt["Volume"], dt["SL"]] 
        return tickers

    def clear_all(collection):
        collection = db[collection]
        collection.delete_many({})

class Orders():
    def save_buy_order(collection, symbol, orderId, origQty, cummulativeQuoteQty, avgPrice):
        collection = db[collection]
        new_order = {"Symbol":symbol, "OrderId":orderId, "Quantity":origQty, "Amount":cummulativeQuoteQty,
                        "BuyPrice":avgPrice}
        data = collection.insert_many(new_order)
        return data

    def save_oco_order(collection, symbol, orderId, origQty, take_profit, stop_limit, trigger_price):
        collection = db[collection]
        new_order = {"Symbol":symbol, "OrderId":orderId, "Quantity":origQty,
                        "TP":take_profit, "SL":stop_limit, "Trigger":trigger_price}
        data = collection.insert_many(new_order)
        return data

    def save_buy_market_okex(collection, symbol, orderId, origQty, amount, avgPrice):
        collection = db[collection]
        new_order = {"Symbol":symbol, "OrderId":orderId, "Quantity":origQty, "Amount":amount,
                        "BuyPrice":avgPrice}
        data = collection.insert_one(new_order)
        return data 

    def find_all_buy_market_okex(collection):
        tickers = []
        collection = db[collection]
        data = collection.find({})
        index = 0
        for dt in data:
            tickers.append({"Symbol":dt["Symbol"],"Quantity":dt["Quantity"],"BuyPrice": dt["BuyPrice"],"Amount": dt["Amount"],"OrderId": dt["OrderId"],"_id": dt["_id"]}) 
            index +=1 
        return index,tickers       

    
    def delete_buy_market_okex(collection,order_id):
        collection = db[collection]
        query = {'OrderId':order_id}
        collection.delete_one(query)    




