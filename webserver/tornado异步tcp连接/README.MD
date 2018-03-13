# tornado 异步tcp连接

> tornado 有TCPClient 和 TCPServer 两个类，可用于实现tcp的客户端和服务端。都是对iostream的简单包装

## iostream

- iostream 是client和server之间的tcp通道
- 被动等待创建iostream的一方是server，主动找对方创建iostream的一方是client
- 在iostream创建之后client于server的操作再无分别是，在人和时候都可以通过iostream.write 向对方传送内容，或者通过iostream.read* 接受对方传来的内容。或者iostream.close关闭连接
1. read_bytes 读取指定长度
2. read_until 读取直到特定字符
3. read_until_regex 读取直到特定的正则表达式
4. read_until_close读取直到链接关闭

## TCPServer

1. 创建一个继承于TCPServer类的实例，监听端口，启动服务器
2. 启动消息循环
3. 服务器开始运行
4. client连接过来 tornado会创建一个iostream，然后调用handle_strem方法，调用时，传入的两个参数是iostream和client的地址
