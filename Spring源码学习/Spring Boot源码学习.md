### Spring Boot源码学习

#### Spring Boot的启动流程

启动流程图地址（https://www.processon.com/view/link/59812124e4b0de2518b32b6e）

![image-20200817153838516](C:\Users\itanc\AppData\Roaming\Typora\typora-user-images\image-20200817153838516.png)

基于Spring Boot 2.1.5，非Spring的代码只有下面这图中的代码：

```java
@SpringBootApplication
public class App {
    public static void main(String[] args) {
        SpringApplication application = new SpringApplication(AppServer.class);
        application.run(args);
    }
}
```

#### 构造函数

SpringApplication的构造函数实例化了  **初始化上下文的各种接口**——ApplicationContextInitializer以及监听器——ApplicationListener，要注意的是这里的实例化













































