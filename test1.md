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