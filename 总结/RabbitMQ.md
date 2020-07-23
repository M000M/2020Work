## RabbitMQ

brew install rabbitmq

安装图形管理工具

**sudo sbin/rabbitmq-plugins enable rabbitmq_management**

默认配置的端口：localhost:15672

**添加用户**

![截屏2020-05-22 上午11.29.53](/Users/didi/Desktop/截屏2020-05-22 上午11.29.53.png)

virtual host就相当于MySQL的 db

**添加vhost**

![截屏2020-05-22 上午11.32.36](/Users/didi/Desktop/截屏2020-05-22 上午11.32.36.png)

一般以/开头

得对用户进行授权

![截屏2020-05-22 上午11.37.27](/Users/didi/Desktop/截屏2020-05-22 上午11.37.27.png)





### 简单队列

#### 1.1 模型

<img src="/Users/didi/Library/Application Support/typora-user-images/image-20200522114659108.png" alt="image-20200522114659108" style="zoom: 50%;" />

P：消息生产者

队列

C：消费者

3个对象  生产者   队列    消费者



### 1.2获取MQ连接





































