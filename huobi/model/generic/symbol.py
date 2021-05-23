class Symbol:
    """
    The Huobi supported symbols.

    :member
        base_currency: The base currency in a trading symbol.
        quote_currency: The quote currency in a trading symbol.
        price_precision: The quote currency precision when quote price (decimal places).
        amount_precision: The base currency precision when quote amount (decimal places).
        symbol_partition: The trading section, possible values: [main，innovation，bifurcation].
        symbol: The symbol, like "btcusdt".
        state : trade status, maybe one in [online，offline,suspend]
        value_precision : value precision
        min_order_amt : minimum volume limit only used in limit-order and sell-market order
        max_order_amt : Maximum volume
        min_order_value : Minimum order amount
        leverage_ratio : Leverage ratio for symbol
        limit_order_min_order_amt: Minimum order amount of limit order in base currency (NEW)
        limit_order_max_order_amt: Max order amount of limit order in base currency (NEW)
        sell_market_min_order_amt: Minimum order amount of sell-market order in base currency (NEW)
        sell_market_max_order_amt: Max order amount of sell-market order in base currency (NEW)
        buy_market_max_order_amt: Max order value of buy-market order in quote currency (NEW)
        max_order_value: Max order value of limit order and buy-market order in usdt (NEW)
    Base Currency : nest  基础币种名称
	Quote Currency : eth  报价币种
	Price Precision : 8   价格小数位
	Amount Precision ：2  报单数量小数位
	Symbol Partition : innovation   所在的板块   main 主板 可能值: [main，innovation]
	Symbol : nesteth        交易对
	State : online      [online，offline,suspend] online - 已上线；offline - 交易对已下线，不可交易；suspend -- 交易暂停；pre-online - 即将上线
	Value Precision : 8     交易对交易金额的精度
	Min Order Amount : 1    交易对限价单最小下单量 ，以基础币种为单位（即将废弃）
	Max Order Amount : 25000000    交易对限价单最大下单量 ，以基础币种为单位（即将废弃）
	Min Order Value : 0.01         交易对限价单和市价买单最小下单金额 ，以计价币种为单位
	Leverage Ratio : 0             交易对杠杆最大倍数
	Minimum order amount (Limit Order) : 1
	Max order amount (Limit Order) : 25000000
	Min order amount (Sell Market Order) : 1
	Max order amount (Sell Market Order) : 2500000
	Max order value (Buy Market Order) : 400
	Max order value (In USDT) : 0
    """

    def __init__(self):
        self.base_currency = ""
        self.quote_currency = ""
        self.price_precision = 0
        self.amount_precision = 0
        self.symbol_partition = ""
        self.symbol = ""
        self.state = ""
        self.value_precision = 0
        self.min_order_amt = ""
        self.max_order_amt = ""
        self.min_order_value = ""
        self.leverage_ratio = 0
        self.limit_order_min_order_amt = 0
        self.limit_order_max_order_amt = 0
        self.sell_market_min_order_amt = 0
        self.sell_market_max_order_amt = 0
        self.buy_market_max_order_value = 0
        self.max_order_value = 0

    def print_object(self, format_data=""):
        from huobi.utils.print_mix_object import PrintBasic
        PrintBasic.print_basic(self.base_currency, format_data + "Base Currency")
        PrintBasic.print_basic(self.quote_currency, format_data + "Quote Currency")
        PrintBasic.print_basic(self.price_precision, format_data + "Price Precision")
        PrintBasic.print_basic(self.amount_precision, format_data + "Amount Precision")
        PrintBasic.print_basic(self.symbol_partition, format_data + "Symbol Partition")
        PrintBasic.print_basic(self.symbol, format_data + "Symbol")
        PrintBasic.print_basic(self.state, format_data + "State")
        PrintBasic.print_basic(self.value_precision, format_data + "Value Precision")
        PrintBasic.print_basic(self.min_order_amt, format_data + "Min Order Amount")
        PrintBasic.print_basic(self.max_order_amt, format_data + "Max Order Amount")
        PrintBasic.print_basic(self.min_order_value, format_data + "Min Order Value")
        PrintBasic.print_basic(self.leverage_ratio, format_data + "Leverage Ratio")
        PrintBasic.print_basic(self.limit_order_min_order_amt, format_data + "Minimum order amount (Limit Order)")
        PrintBasic.print_basic(self.limit_order_max_order_amt, format_data + "Max order amount (Limit Order)")
        PrintBasic.print_basic(self.sell_market_min_order_amt, format_data + "Min order amount (Sell Market Order)")
        PrintBasic.print_basic(self.sell_market_max_order_amt, format_data + "Max order amount (Sell Market Order)")
        PrintBasic.print_basic(self.buy_market_max_order_value, format_data + "Max order value (Buy Market Order)")
        PrintBasic.print_basic(self.max_order_value, format_data + "Max order value (In USDT)")
