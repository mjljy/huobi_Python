#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:LJY
# datetime:2021/5/23 
# software: Vscode
from huobi.client.generic import GenericClient
from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.utils import *
import time






def main():
    # pass
    generic_client = GenericClient()
    list_obj = generic_client.get_exchange_symbols()
    usdt_list_symbol = []
    for bizhong in list_obj:
        if bizhong.quote_currency == "usdt":
            usdt_list_symbol.append(bizhong)
    LogInfo.output("-----火币usdt交易区总币种有 {} 个----".format(len(usdt_list_symbol)))
    market_client = MarketClient()
    vol_100w = []
    vol_100w_500w =[]
    vol_500w_1000w =[]
    vol_5000w_1000w =[]
    vol_5000w_1y =[]
    vol_1y_5y =[]
    vol_5y_10y =[]
    vol_10y_20y =[]
    vol_20y_50y =[]
    vol_50y_100y =[]
    vol_100y =[]
    '''for bizhong in usdt_list_symbol  :
        # if bizhong.state == "online" and bizhong.base_currency == 'sushi':
        if bizhong.state == "online":
            tradeinfo = market_client.get_market_detail(bizhong.symbol)
            if tradeinfo.vol * 6.79 <= 1000000:#小于100w
                vol_100w.append(bizhong.base_currency)
            if 5000000 > tradeinfo.vol * 6.79 >= 1000000:
                vol_100w_500w.append(bizhong.base_currency)
            if 10000000 > tradeinfo.vol * 6.79 >= 5000000:
                vol_500w_1000w.append(bizhong.base_currency)
            if 50000000 > tradeinfo.vol * 6.79 >= 10000000:
                vol_5000w_1000w.append(bizhong.base_currency)
            if 100000000 >tradeinfo.vol * 6.79 >= 50000000:
                vol_5000w_1y.append(bizhong.base_currency)
            if 500000000 >tradeinfo.vol * 6.79 >= 100000000:
                vol_1y_5y.append(bizhong.base_currency)
            if 1000000000 >tradeinfo.vol * 6.79 >= 500000000 :
                vol_5y_10y.append(bizhong.base_currency)
            if 2000000000>tradeinfo.vol * 6.79 >= 1000000000 :
                vol_10y_20y.append(bizhong.base_currency)
            if 5000000000>tradeinfo.vol * 6.79 >= 2000000000 :
                vol_20y_50y.append(bizhong.base_currency)
            if 10000000000>tradeinfo.vol * 6.79 >= 5000000000 :
                vol_50y_100y.append(bizhong.base_currency)
            if tradeinfo.vol * 6.79 >= 10000000000 :
                vol_100y.append(bizhong.base_currency)'''
        # if bizhong.base_currency == 'sushi':
            # tradeinfo.print_object()



        # time.sleep(0.01)
    # print('小于100w',vol_100w)
    # print('--------------------------------------')
    # print('小于500w 大于100w',vol_100w_500w)
    # print('--------------------------------------')
    # print('小于1000w 大于500w',vol_500w_1000w)
    # print('--------------------------------------')
    # print('小于5000w 大于1000w',vol_5000w_1000w)
    # print('--------------------------------------')
    # print('小于1y 大于5000w',vol_5000w_1y)
    # print('--------------------------------------')
    # print('大于1y_5y',vol_1y_5y)
    # print('--------------------------------------')
    # print('大于5y_10y',vol_5y_10y)
    # print('--------------------------------------')
    # print('大于10y_20y',vol_10y_20y)
    # print('--------------------------------------')
    # print('大于20y_50y',vol_20y_50y)
    # print('--------------------------------------')
    # print('大于50y_100y',vol_50y_100y)
    # print('--------------------------------------')
    # print('大于100y',vol_100y)
    # print('小于500w 大于100w',vol_100w)
    # sysmbol_list= []
    market_client = MarketClient(init_log=True)
    for bizhong in usdt_list_symbol[0:1]:
        interval = CandlestickInterval.DAY1
        # symbol = "ethusdt"
        symbol = bizhong.symbol
        list_obj = market_client.get_candlestick(symbol, interval, 30)
        for candlestick in list_obj:
            # print(candle)
            candlestick.print_object()
    



main()
