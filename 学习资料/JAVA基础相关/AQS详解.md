### AQS详解

所谓AQS，指的是AbstractQueuedSynchronizer，它提供了一种实现阻塞锁和一系列依赖FIFO等待队列的同步器的框架，ReentrantLock、Semaphore、CountDownLatch、CyclicBarrier等并发类均是基于AQS来实现的，具体用法是通过集成AQS实现其模板方法，然后将子类作为同步组件的内部类。

了解一个框架最好的方式是读源码。

AQS是JDK1.5之后才出现的。

#### 基本框架

AQS的基本思想及其相关概念。

AQS的基本框架如下图所示：

![image-20200823233752934](C:\Users\itanc\AppData\Roaming\Typora\typora-user-images\image-20200823233752934.png)

AQS维护了一个volatile语义（支持多线程下的可见性）的共享资源变量state和一个FIFO线程等待队列（多线程竞争state被阻塞时会进入此队列）。

#### State

共享资源变量state，它是int数据类型的，其访问方式有3种：

- getState()
- setState(int newState)
- compareAndSetState(int expect, int update)

上述3中方式均是原子操作，其中compareAndSetStatus()的实现依赖于Unsafe的compareAndSwapInt()方法。

![image-20200823234237077](C:\Users\itanc\AppData\Roaming\Typora\typora-user-images\image-20200823234237077.png)

具有内存读可见性语义



![image-20200823234310116](C:\Users\itanc\AppData\Roaming\Typora\typora-user-images\image-20200823234310116.png)

具有内存写可见性语义



![image-20200823234341072](C:\Users\itanc\AppData\Roaming\Typora\typora-user-images\image-20200823234341072.png)

具有内存读/写可见性语义



资源的共享方式为2种：

- 独占式(Exclusive)

  只有单个线程能够成功获取资源并执行，如ReentrantLock。

- 共享式(Shared)

  多个线程可成功获取资源并执行，如Semaphore/CountDownLatch等。

AQS将大部分的同步逻辑均已经实现好，继承的自定义同步器只需要实现state的获取(acquire)和释放(release)的逻辑代码就可以，主要包括下面方法：

- tryAcquire(int): 独占方式。尝试获取资源，成功返回true，失败返回false;
- tryRelease(int): 独占方式。尝试释放资源，成功返回true，失败返回false;
- tryAcquireShared(int): 共享方式。尝试获取资源。负数表示失败；0表示成功，但没有剩余可用资源；正数表示成功，且有剩余资源;
- tryReleaseShared(int): 共享方式。尝试释放资源，如果释放后允许唤醒后续等待结点返回true，否则返回false;
- isHeldExclusively(): 该线程是否正在独占资源。只有用到condition才会去实现它。

AQS需要子类覆写的方法均没有声明为abstract，目的是避免子类需要强制性覆写多个方法，因为一般自定义同步器要么是独占方法，要么是共享方法，只需实现tryAcquire-tryRelease、tryAcquireShared-tryReleaseShared中的一种即可。

当然，AQS也支持子类同时实现独占和共享两种模式，如ReentrantReadWriteLock。

#### CLH队列（FIFO）

AQS通过内部类Node来实现FIFO队列，源代码解析如下：

```java
/** CLH Nodes */
abstract static class Node {
    volatile Node prev;       // initially attached via casTail
    volatile Node next;       // visibly nonnull when signallable
    Thread waiter;            // visibly nonnull when enqueued
    volatile int status;      // written by owner, atomic bit ops by others

    // methods for atomic operations
    final boolean casPrev(Node c, Node v) {  // for cleanQueue
        return U.weakCompareAndSetReference(this, PREV, c, v);
    }
    final boolean casNext(Node c, Node v) {  // for cleanQueue
        return U.weakCompareAndSetReference(this, NEXT, c, v);
    }
    final int getAndUnsetStatus(int v) {     // for signalling
        return U.getAndBitwiseAndInt(this, STATUS, ~v);
    }
    final void setPrevRelaxed(Node p) {      // for off-queue assignment
        U.putReference(this, PREV, p);
    }
    final void setStatusRelaxed(int s) {     // for off-queue assignment
        U.putInt(this, STATUS, s);
    }
    final void clearStatus() {               // for reducing unneeded signals
        U.putIntOpaque(this, STATUS, 0);
    }

    private static final long STATUS
        = U.objectFieldOffset(Node.class, "status");
    private static final long NEXT
        = U.objectFieldOffset(Node.class, "next");
    private static final long PREV
        = U.objectFieldOffset(Node.class, "prev");
}

// Concrete classes tagged by type
static final class ExclusiveNode extends Node { }
static final class SharedNode extends Node { }

static final class ConditionNode extends Node
    implements ForkJoinPool.ManagedBlocker {
    ConditionNode nextWaiter;            // link to next waiting node

    /**
         * Allows Conditions to be used in ForkJoinPools without
         * risking fixed pool exhaustion. This is usable only for
         * untimed Condition waits, not timed versions.
         */
    public final boolean isReleasable() {
        return status <= 1 || Thread.currentThread().isInterrupted();
    }

    public final boolean block() {
        while (!isReleasable()) LockSupport.park();
        return true;
    }
}
```



#### 获取资源（独占模式）

##### acquire(int)

首先讲解独占模式(Exclusive)下的获取/释放资源过程，其入口方法为：

```java
public final void acquire(int arg) {
    if (!tryAcquire(arg))
        acquire(null, arg, false, false, false, 0L);
}
```

tryAcquire(arg)为线程获取资源的方法函数，在AQS中定义如下：

```java
protected boolean tryAcquire(int arg) {
    throw new UnsupportedOperationException();
}
```

很明显，该方法是空方法，且由protected修饰，说明该方法需要由子类即自定义同步器来实现。

























































