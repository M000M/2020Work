## 常用Linux命令

- 查看Linux系统负载

    top

- 查看当前系统的总内存大小以及使用内存的情况

    free

- 查看进程

    ps aux 或 ps -ef，结合管道符一起使用，查看某个进程或者它的数量；

- 查看端口

    netstat

    netstat -lnp 用于打印当前系统启动了哪些端口

    netstat -an 用于打印网络连接状况

- 抓包工具

    tcpdump

    抓包工具分析数据包，知道有哪些IP在攻击；可以将内容写入文件1.cap中，现实包的内容，不加-w屏幕显示数据流向

- wireshark

    抓包工具，可以临时用该命令查看当前服务器上的web请求



#### cat、tail、vi、vim之间的区别？

tail  [参数] [文件]

- -f 循环读取
- -q 不显示处理信息
- -v 显示详细的处理信息
- -c<数目> 显示的字节数
- -n<行数> 显示文件的尾部 n 行内容
- --pid=PID 与-f合用,表示在进程ID,PID死掉之后结束
- -q, --quiet, --silent 从不输出给出文件名的首部
- -s, --sleep-interval=S 与-f合用,表示在每次反复的间隔休眠S秒

```
tail notes.log    #显示notes.log文件的最后10行
tail -f nodes.log #要跟踪notes.log文件的增长情况，即有其他进程在写notes.log文件，实时的显示出来

tail +20 notes.log #显示文件notes.log内容，从第20行至文件末尾
tail -c 10 notes.log #显示notes.log文件的最后10个字符
```



cat [参数] [文件]

- **-n 或 --number**：由 1 开始对所有输出的行数编号。
- **-b 或 --number-nonblank**：和 -n 相似，只不过对于空白行不编号。
- **-s 或 --squeeze-blank**：当遇到有连续两行以上的空白行，就代换为一行的空白行。
- **-v 或 --show-nonprinting**：使用 ^ 和 M- 符号，除了 LFD 和 TAB 之外。
- **-E 或 --show-ends** : 在每行结束处显示 $。
- **-T 或 --show-tabs**: 将 TAB 字符显示为 ^I。
- **-A, --show-all**：等价于 -vET。
- **-e：**等价于"-vE"选项；
- **-t：**等价于"-vT"选项；

### 实例：

把 textfile1 的文档内容加上行号后输入 textfile2 这个文档里：

```
cat -n textfile1 > textfile2
```

把 textfile1 和 textfile2 的文档内容加上行号（空白行不加）之后将内容附加到 textfile3 文档里：

```
cat -b textfile1 textfile2 >> textfile3
```

清空 /etc/test.txt 文档内容：

```
cat /dev/null > /etc/test.txt
```

cat 也可以用来制作镜像文件。例如要制作软盘的镜像文件，将软盘放好后输入：

```
cat /dev/fd0 > OUTFILE
```

相反的，如果想把 image file 写到软盘，输入：

```
cat IMG_FILE > /dev/fd0
```