### IOC

实现IOC的原理是 **<u>反射</u>**

```java
package demo.controller;

import demo.service.UserService;

public class UserController {
    private UserService userService;

    public UserService getUserService() {
        return userService;
    }

    public void setUserService(UserService userService) {
        this.userService = userService;
    }
}
```

```java
package demo.service;

public class UserService {
}
```

```java
package demo;

import demo.controller.UserController;
import demo.service.UserService;
import org.junit.Test;

import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class Demo {

    @Test
    public void test() throws Exception {
        UserController userController = new UserController();
        System.out.println(userController.getUserService());

        Class<? extends UserController> clazz = userController.getClass();
        // 创建对象
        UserService userService = new UserService();
        System.out.println(userService);
        // 获取所有的属性
        Field serviceField = clazz.getDeclaredField("userService");
        serviceField.setAccessible(true); //设置可见性
        // 只有通过方法才能获得具体的属性
        String name = serviceField.getName().substring(0, 1).toUpperCase() + serviceField
                .getName().substring(1);
        String setMethodName = "set" + name;
        // t通过方法注入属性的对象
        Method method = clazz.getMethod(setMethodName, UserService.class);
        // 反射
        method.invoke(userController, userService);
        System.out.println(userController.getUserService());
    }
}
```

<img src="C:\Users\itanc\AppData\Roaming\Typora\typora-user-images\image-20200804224026953.png" alt="image-20200804224026953" style="zoom:67%;" />

通过获取UserController对象里面的属性，设置可见性，再通过**<u>反射</u>**将属性注入进去。

```java
package demo.controller;

import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
@Inherited
@Documented
public @interface AutoWried {
}
```



在属性上标注注解，对标注了注解的属性注入对象

```java
package demo;

import demo.controller.AutoWried;
import demo.controller.UserController;
import demo.service.UserService;
import org.junit.Test;

import java.lang.annotation.Annotation;
import java.lang.reflect.Type;
import java.util.stream.Stream;

public class Demo2 {

    @Test
    public void test() {
        UserController userController = new UserController();
        Class<? extends UserController> clazz = userController.getClass();
        Stream.of(clazz.getDeclaredFields()).forEach(field->{
            Annotation annotation = field.getAnnotation(AutoWried.class);
            if (annotation != null) {
                field.setAccessible(true);
                // 获取属性的类型
                Class<?> type = field.getType();
                try {
                    Object o = type.newInstance();
                    field.set(userController, o);
                } catch (InstantiationException e) {
                    e.printStackTrace();
                } catch (IllegalAccessException e) {
                    e.printStackTrace();
                }
            }
        });
        System.out.println(userController.getUserService());
    }
}
```

<img src="C:\Users\itanc\AppData\Roaming\Typora\typora-user-images\image-20200804223936866.png" alt="image-20200804223936866" style="zoom:67%;" />

获取标注了注解的属性，设置属性的可见性，获得属性的类型，根据类型创建一个类的对象，将该对象赋值给该对象的属性，这样就完成了依赖注入。



通过这些Map存储对象，有单例的对象，也有多例的对象

```
DefaultListableBeanFactory类实现了ListableBeanFactory接口，ListableBeanFactory接口扩展至BeanFactory接口
在DefaultListableBeanFactory中可以看到通过这几个Map结构来存储对象
```

![image-20200804232448675](C:\Users\itanc\AppData\Roaming\Typora\typora-user-images\image-20200804232448675.png)



可以看到BeanFactory接口以下的集成关系图

![image-20200804232840961](C:\Users\itanc\AppData\Roaming\Typora\typora-user-images\image-20200804232840961.png)



