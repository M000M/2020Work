# Docker

## 什么是Docker

### 开发和运维的环境不一样可能导致发布问题

### Docker就是解决这个问题的

- 运维带环境安装

### 在哪

- 官网

	- www.docker.com
	- www.docker-cn.com

- 仓库

	- Docker Hub

		- hub.docker.com

## Docker能干什么

### 之前的虚拟化技术

- 虚拟机就是带环境安装的一种解决方案。它可以在一种操作系统里面运行另一种操作系统，比如在Windows系统里面运行Linux系统。引用程序对此毫无感知，因为虚拟机看上去跟真实系统一模一样，而对底层系统来说，虚拟机就是一个普通文件，不需要了就删掉，对其他部分毫无影响。这类虚拟机完美的运行了另外一套系统，能够使应用程序、操作系统和硬件三者之间的逻辑不变

	- 资源占用多
	- 冗余步骤多
	- 启动慢

### 容器虚拟化技术

- 由于前面的虚拟机存在这些缺点，Linux发展出了另一种虚拟化技术：Linux容器（Linux Container， LXC）

	- Linux容器不是模拟一个完整的操作系统，而是对进程进行隔离
	- 有了容器，就可以将软件运行所需的所有资源打包到一个隔离的容器中
	- 容器和虚拟机不同，不需要捆绑一整套操作系统，只需要软件工作所需的库资源和设置。系统因此而变得高效并保证部署在任何环境中的软件都能始终如一地运行

### 比较Docker和传统虚拟机的不同之处

- 传统虚拟机技术是虚拟出一套硬件之后，在骑上运行一个完整的操作系统
- 而容器内的应用进程直接运行与宿主的内核，容器内没有自己的内核，也没有进行硬件虚拟，因此容器要比传统虚拟机更轻便
- 每个容器之间相互隔离，每个容器有自己的文件系统，容器之间进程不会相互影响，能区分计算资源
- Docker就是一个缩小版、高度浓缩的Linux虚拟机系统

### 开发/运维(DevOps)

### 企业级

## 安装Docker

### 前提说明

- CentOS在6.5以上的版本

### Docker的基本组成

- Docker的架构图

### 安装步骤

### Hello World

### Subtopic 5

## Docker常用命令

## Docker镜像

## Docker容器数据卷

## DockerFile解析

## Docker常用安装

## 本地镜像发布到阿里云

*XMind - Trial Version*