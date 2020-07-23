## Redis总结	

### string

**set** key value

**get** key

**del** key

**mset** key1 value1 key2 value2 ...

**mget** key1 key2 ...

获取数据字符个数（字符串长度） 

**strlen** key

追加信息到原始信息后部（如果原始信息存在就加，否则新建）

**append** key value



#### 设置数值数据增加指定范围的值

**incr** key

**incrby** key increment

**incrbyfloat** key increment



#### 设置数值数据减少制定范围的值

**decr** key

**decrby** key increment

**按数值进行操作的数据，如果原始数据不能转换为数值，或则超过了Redis数值范围上限，将报错。**



#### 设置数据具有指定的生命周期

**setex** key seconds value

**psetex** key milliseconds value

Redis控制数据的生命周期，通过数据是否失效控制业务行为，适用于所有具有时效性限定控制的操作



常用于存储的格式：

**表名:主键名:主键值 value**





### hash

**hset** key field value

**hget** key field

**hgetall** key

**hdel** key field



**hmset** key field1 value1, field2 value2, ......

**hmget** key field1, field2, .......



**hkeys** key

**hvals** key



**hincrby** key field increment

**hincrbyfloat** key field increment

hash类型下的value只能存储字符串，不能再嵌套存储其他类型的数据

每个hash可以存储2^32 - 1个键值对

hash的设计初衷不是为了存储对象的，因此不可滥用

hgetall操作可以获取全部属性，如果内部field过多，效率很低



string存储对象（json）与hash存储对象，string在于存储，hash在于修改



**购物车实现**

以用户ID作为key，商品编号作为field，商品数量作为value

当前仅仅是将数据存储到了Redis中，宾没有起到加速的作用，商品信息还需要二次查询数据库

- 每条购物车中的商品记录保存成两条field

- field1专用于保存购买数量

  命名格式：商品ID：nums

  保存数据：数值

- field2专用于保存购物车中显示的信息，包含文字描述，图片地址，所属商家信息等

  命名格式：商品ID：info

  保存数据：json 

  hmset 001 g01:nums 2 g01:info {......}

商品信息可以独立hash，这样可以大大减少重复的信息

**hsetnx** key field value



商家应用

- 以商家ID作为key
- 将参与抢购的商品ID作为field
- 将参与抢购的商品数量作为对应的value
- 抢购时使用降值的方式控制产品的数量

<u>Redis通常只做数据的提供和保存，尽量不要把业务压到Redis上</u>

Tips5：

Redis应用于抢购，限购类、限量发放优惠卷、激活码等业务的数据存储设计



### list

添加/修改

**lpush** key value1 [value2]....

**rpush** key value1 [value2]....

获取数据

**lrange** key start stop    (0, -1显示所有数据)

**lindex** key index

**llen** key

获取并移除数据

**lpop** key

**rpop** key



规定时间内获取并移除数据

**blpop** key1 [key2] timeout

**brpop** key1 [key2] timeout



朋友圈点赞，按照点赞顺序现实好友的点赞信息

如果取消点赞，移除对应好友信息

- 移除指定数据

> **lrem** key count value （value为从左边开始删除指定个数的value）



Tips6:

<u>redis应用于具有操作先后顺序的数据控制</u>



list中保存的数据都是string类型的，数据总量是有限的

list中最多保存2^32  - 个元素

list具有索引的概念，但是操作数据时通常以队列的形式进行入队操作，或以栈的形式进行入栈出栈操作

获取全部数据操作结束索引设置为-1

list可以对数据进行分页操作，通常第1页的信息来自于list，第2页及更多的信息通过数据库的形式加载



应用场景

微博/twitter关注列表/粉丝列表，先关注的在前面；

新闻、咨询类网站如何将新闻或咨询按照发生的时间顺序展示；

企业运营过程中，系统将产生大量的运营数据，如何保障多台服务器操作日志的统一顺序输出？（每个服务器都往Redis中写）

**解决方案**

- 依赖list的数据具有顺序的特征对信息进行管理
- 使用队列模型解决多路信息汇总合并的问题
- 使用栈模型解决最新消息的问题

 



### set

添加数据

**sadd** key member1 [member2]

获取全部数据

**smembers** key

删除数据

**srem** key member1 [member2]

获取集合数据总量

**scard** key

判断集合中是否包含指定数据

**sismember** key member

























































