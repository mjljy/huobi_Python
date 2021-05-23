#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:LJY
# datetime:2021/1/1 20:37
# software: PyCharm
from huobi.client.generic import GenericClient
from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.utils import *
from config import bi_0_50w, bi_50_100w, bi_100_500w, bi_500_1000w, bi_10000w
import time
from huobi.utils import *
def Get_bi_usdt():
    '''
    查询货币usdt交易区的所有币种
    :return: usdt_list_symbol    symbol元素组成的列表

    '''
    generic_client = GenericClient()
    list_obj = generic_client.get_exchange_symbols()
    # if len(list_obj):
        # for idx, row in enumerate(list_obj):
            # LogInfo.output("------- number " + str(idx) + " -------")
            # row.print_object()

    usdt_list_symbol = []
    # LogInfo.output("-----火币交易总币种有 {} 个----".format(len(my_list.symbol_list)))
    LogInfo.output("-----火币交易总币种有 {} 个----".format(len(list_obj)))
    for bizhong in list_obj:
        if bizhong.quote_currency == "usdt":
            usdt_list_symbol.append(bizhong)
    LogInfo.output("-----火币usdt交易区总币种有 {} 个----".format(len(usdt_list)))
    return  usdt_list_symbol

def Get_bi_vol(usdt_list_symbol):
    '''
    计算货币usdt交易区的币种成交量 并按照成交量来排序
    :param usdt_list:
    :return:
    '''
    generic_client = GenericClient()
    global bi_0_50w, bi_50_100w, bi_100_500w, bi_500_1000w, bi_10000w
    for bizhong in usdt_list_symbol:
        if bizhong.state == "online":
            tradeinfo = my_client.get_24h_trade_statistics(bizhong.symbol)
            if 1000000 > tradeinfo.volume * 6.79 >= 500000:
                bi_50_100w.append(bizhong.base_currency)
            if 5000000 > tradeinfo.volume * 6.79 >= 1000000:
                bi_100_500w.append(bizhong.base_currency)
            if 10000000 > tradeinfo.volume * 6.79 >= 5000000:
                bi_500_1000w.append(bizhong.base_currency)
            if tradeinfo.volume * 6.79 >= 10000000:
                bi_10000w.append(bizhong.base_currency)
        time.sleep(0.05)


def strtime_to_stamp(time_str = "2020-01-01 00:00:00"):
    '''
    指定字符串类型转为 时间戳类型
    :return:
    '''
    struct_time = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    #print(struct_time)
    #print(int(time.mktime(struct_time)))
    time_stamp = int(time.mktime(struct_time))
    return time_stamp

def stamp_to_strtime(stamp = 1621767279.0434983):
    '''
    指定时间戳转化为字符串
    :return:
    '''
    # struct_time = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    #print(struct_time)
    #print(int(time.mktime(struct_time)))
    str_time = int(time.ctime(stamp))
    return str_time

# strtime_to_stamp()
# import time

# print(time.ctime(235491790))
# Get_bi_usdt()