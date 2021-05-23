from huobi.client.market import MarketClient

market_client = MarketClient()
obj = market_client.get_market_detail("btcusdt")
print(type(obj))
obj.print_object()



