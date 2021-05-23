#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:LJY
# datetime:2021/5/23 
# software: Vscode
from huobi.client.generic import GenericClient
from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.utils import *
import collections
import time
import time
# print (time.time())
# print (time.ctime(time.time()))
# print (time.localtime(time.time()))


generic_client = GenericClient()
list_obj = generic_client.get_exchange_symbols()
usdt_list_symbol = []
for bizhong in list_obj:
    if bizhong.quote_currency == "usdt" and bizhong.base_currency in('bsv3s','uni2l'):
        # usdt_list_symbol.append(bizhong)
        bizhong.print_object()