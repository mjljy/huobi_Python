1.把筛选币的策略  搞起来



代码的结构分析
1>example
 1_1>
 1_2>
 1_3>
 1_4>generic 普通的

2>huobi
 2_1>client  客户端 
  2_1_6>market  MarketClient 行情     
  get_candlestick  从执行的时间点开始 入参  时间段 1min  5min  1day  数据量 max 200 default 150默认     不能指定时间段
  sub_candlestick    
  req_candlestick   区别？


  get_market_detail  Get trade statistics in 24 hours.  获取24小时行情
  sub_market_detail
  req_market_detail  



3>performance
4>test1
5>tests
6>





策略：
1.成交金额的列表 已经做好
2.上涨日期的判断
  循环 
  第一天 开盘价和收盘价  判断



小于100w ['ltc3l', 'lba', 'link3l', 'eos3l', 'bch3l', 'fil3l']
--------------------------------------
小于500w 大于100w ['ctxc', 'eth1s', 'gof', 'dock', 'can', 'for', 'lhb', 'abt', 'hot', 'insur', 'btc1s', 'wnxm', 'em', 'kan', 'ring', 'mln', 'firo', 'uip', 'wtc', 'mta', 'vsys', 'xrp3l', 'pearl', 'yam', 'swrv', 'fti', 'bcha', 'cnns', 'let', 'xrt', 'pvt', 'ast', 'lxt', 'nuls', 'wbtc', 'dot2l', 'smt', 'df', 'cvp', 'bor', 'pax', 'front', 'utk', 'stn', 'nbs', 'hbc', 'kcash', 'atp', 'stake', 'nhbtc', 'glm', 'xmx', 'dht']
--------------------------------------
小于1000w 大于500w ['bnt', 'stpt', 'arpa', 'tnb', 'wxt', 'act', 'mass', 'node', 'dcr', 'nas', 'filda', 'fsn', 'api3', 'itc', 'ela', 'cvc', 'egt', 'ctsi', 'steem', 'zec3l', 'auction', 'apn', 'beth', 'hit', 'swftc', 'bhd', 'uni2l', 'pond', 'value', 'rai', 'uuu', 'bix', 'nest', 'vidy', 'blz', 'skm']
--------------------------------------
小于5000w 大于1000w ['ren', 'o3', 'nano', 'lat', 'trb', 'nu', 'dka', 'hpt', 'bal', 'icx', 'one', 'xem', 'ar', 'wicc', 'nsure', 'iotx', 'bts', 'ckb', 'ltc3s', 'seele', 'badger', 'lol', 'aac', 'waxp', 'enj', 'reef', 'dai', 'ankr', 'mask', 'nexo', 'rlc', 'loom', 'cru', 'skl', 'forth', 'axs', 'oxt', 'ruff', 'ae', 'ogn', 'bsv3l', 'ekt', 'hc', 'gt', 'ant', 'bat', 'gnx', 'akro', 'lrc', 'dot2s', 'eth3l', 'bsv3s', 'ach', 'pai', 'uma', 'iris', 'elf', 'nkn', 'snt', 'inj', 'cro', 'ogo', 'band', 'mxc', 'cre', 'hive', 'knc', 'mir', 'rvn', 'sc', 'dac', 'pols', 'fis', 'zec3s', 'bags', 'uni2s', 'lamb']
--------------------------------------
小于1y 大于5000w ['avax', 'zil', 'iota', 'btc3l', 'fil3s', 'mkr', 'xch', 'mds', 'eos3s', 'xtz', 'cmt', 'woo', 'tt', 'rndr', 'mana', 'btc3s', 'waves', 'ocn', 'ftt', 'pha', 'zrx', 'mx', 'titan', 'usdc', 'zks', 'soc', 'yfii', 'chr', 'top', 'iost', 'flow', 'yee', 'btm', 'rsr']
--------------------------------------
大于1y_5y ['lina', 'neo', 'atom', '1inch', 'dash', 'hbar', 'yfi', 'omg', 'luna', 'xrp3s', 'xlm', 'xmr', 'new', 'mdx', 'zen', 'kava', 'vet', 'snx', 'crv', 'jst', 'cspr', 'grt', 'comp', 'sol', 'link3s', 'algo', 'storj', 'near', 'eth3s', 'sun', 'theta', 'chz', 'sand', 'ont', 'zec', 'ksm', 'qtum', 'dta', 'bch3s', 'gxc']
--------------------------------------
大于5y_10y ['aave', 'matic', 'icp', 'sushi', 'uni', 'bsv']
--------------------------------------
大于10y_20y ['bch', 'etc', 'link', 'eos', 'ada', 'trx', 'nft']
--------------------------------------
大于20y_50y ['shib', 'xrp', 'ltc', 'dot', 'doge', 'fil', 'ht', 'btt']
--------------------------------------
大于50y_100y []
--------------------------------------
大于100y ['eth', 'btc']




