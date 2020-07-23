### MacOS安装MySQL并设置开机时自动启动服务

#### 1.安装mysql

brew install mysql

(如果要安装指定版本的mysql，brew install mysql@8.0，安装8.0版本的)

#### 2.启动MySQL

mysql.server start 启动mysql服务

mysql.server stop 停止mysq服务

#### 3.修改root密码

第一次登陆时不需要密码

mysql -uroot 回车

注意，在mysql8.0+版本上修改密码时与以往版本不同

use mysql; 

**alter user 'root'@localhost IDENTIFIED BY '新密码'**

#### 4.将mysql服务设置为系统进程，当系统启动时就会启动MySQL

在 mysql的安装目录下，/usr/local/opt/mysql，系统默认的安装路径

有一个文件 homebrew.mxcl.mysql.plist

将它拷贝到 /Library/LaunchAgents目录下

sudo cp /usr/local/opt/mysql/homebrew.mxcl.mysql.plist /Library/LaunchAgents



**launchctl**是Mac OS下用于初始化系统环境的关键进程，它是内核装在成功之后在OS环境下启动的第一个进程

**sudo launchctl load homebrew.mxcl.mysql.plist**

使用 launchctl list可以查看到 homebrew.mxcl.mysql被加载为了一个系统的启动项	

重启系统，mysql就作为系统进程自动启动了

参考：https://www.jianshu.com/p/e73978416920

















