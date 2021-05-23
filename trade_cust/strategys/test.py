#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:LJY
# datetime:2021/1/1 23:25
# software: PyCharm
from huobi.client.generic import GenericClient
from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.utils import *
bi_0_50w = []
bi_50_100w = []
bi_100_500w = []
bi_500_1000w = []
bi_10000w = []
generic_client = GenericClient()
list_obj = generic_client.get_exchange_symbols()
usdt_list = []
usdt_list_symbol = []
LogInfo.output("-----火币交易总币种有 {} 个----".format(len(list_obj)))
for bizhong in list_obj:
    if bizhong.quote_currency == "usdt":
        usdt_list_symbol.append(bizhong)
        usdt_list.append(bizhong.base_currency)
LogInfo.output("-----火币usdt交易区总币种有 {} 个----".format(len(usdt_list)))
# return usdt_list, usdt_list_symbol
for bizhong in usdt_list_symbol:
    if bizhong.state == "online":
        interval = CandlestickInterval.DAY1
        market_client = MarketClient()
        tradeinfo = market_client.get_market_detail(bizhong.symbol, interval, 10)
        print(tradeinfo)
        if 1000000 > tradeinfo.amount * 6.79 >= 500000:
            bi_50_100w.append(bizhong.base_currency)
        if 5000000 > tradeinfo.amount * 6.79 >= 1000000:
            bi_100_500w.append(bizhong.base_currency)
        if 10000000 > tradeinfo.amount * 6.79 >= 5000000:
            bi_500_1000w.append(bizhong.base_currency)
        if tradeinfo.amount * 6.79 >= 10000000:
            bi_10000w.append(bizhong.base_currency)
    time.sleep(0.05)
print(bi_10000w)
print(bi_500_1000w)
print(bi_100_500w)
print(bi_50_100w)
