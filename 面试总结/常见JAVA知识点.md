## 常见JAVA知识点

#### 包装类缓存问题

基本类型数据在跟包装类比较的时候会自动拆箱，即用==跟equals比较的时候，得到的结果是一样的

Integer用一个数组cache[]缓存  -128 ～ 127之间的整数，即调用Integer.of(num)等到的是同一个对象

Boolean：全部缓存 true和false；

Byte：全部缓存，-128 ～ 127；

Character:  <= 127的缓存；

Short:  -128 ~ 127的缓存；

Long:  -128 ～ 127的缓存；

Integer: -128 ~ 127的缓存；

Float:  没有缓存；

Double:  没有缓存



#### 接口要让所有类去实现，因此不能用protected修饰



#### JAVA的IO流相关类的分类、继承关系，结点流和处理流



#### 使用Thread类和Runnable方法来创建一个线程的区别是什么？