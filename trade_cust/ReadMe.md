1.建立自定义文件夹   尝试demo的使用
Rest it has two basic types of method: GET and POST  获取时时的以往信息
There are two types of method for WebSocket client:
Request method: The method name starts with "Request-",  获取指定时间的信息
it will receive the once-off data after sending the request.
Subscription: The method name starts with "Subscribe-",   订阅时时信息 获取往前的时间
it will receive update after sending the subscription.

example
get: get_order, get_matchresult
post: post_create_order, post_batch_cancel_open_order
req: req_order_list
sub: sub_order_update

数据的获取 采用  WebSocket Request

2.linux python 第三方库安装 命令备忘
pip3 install --upgrade pip
pip3  install websocket_client
pip3 install ctyped
