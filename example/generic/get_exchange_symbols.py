from huobi.client.generic import GenericClient
from huobi.utils import *


generic_client = GenericClient()
list_obj = generic_client.get_exchange_symbols()
print(type(list_obj))   # list
#print(list_obj)         # <huobi.model.generic.symbol.Symbol object at 0x7fc3c9fc9590>i

if len(list_obj):
    for idx, row in enumerate(list_obj[0:1]):
        LogInfo.output("------- number " + str(idx) + " -------")
        row.print_object()



