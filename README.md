# tornado 

1. 搭配nginx主要是处理静态内容作为前端代理
2. tornado是异步的，但是是单线程且阻塞式的结构，当处理db以及文件io就会阻塞，将db以及文件io通过nginx代理或者tornado自己的http client路由给其他动态模块处理
3. nginx 提供多进程worker模型，tornado是事件驱动的典型案例，单进程单线程性能的机制，配合nginx，很完美，在根据系统的cpu配置cpu核数配置worker进程数，性能是完美的

## 特点

1、传统多线程框架，

2、tornado 是个基于epoll的单线程web框架，tornado的核心是ioloop

3、ioloop d的核心epoll是个io多路复用器

4、一个主线程可处理所有的异步事件，而且还让你可以以可读性更高的协程方式编写代码，这么做的好处是，没有线程切换，没有多余线程，理论上只要内存足够，并发连接数无上限

## 开发注意
1. tornado 是单线程框架，所有io （redis mysql）请用异步连接器，如果没有可以用线程池来做异步，不然是会阻塞主线程的
2. 非常耗时的cpu计算密集型任务也交由线程池来做，不然其他执行完才会继续
3. 建议服务器有几核Cpu，就起几个tornado服务
4. 配合任务队列celery