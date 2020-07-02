# 什么是容器？
- 用来对应用程序进行隔离的一种虚拟化技术

# 为什么要使用容器？
- 极其轻量：只打包了必要的Bin/Lib；
- 快速部署：根据镜像的不同，容器的部署大概在毫秒与秒之间；
- 易于移植：一次构建，随处部署；

# 容器的主要使用场景
- 容器化传统应用 容器不仅能提高现有应用的安全性和可移植性，还能节约成本。
- 持续集成和持续部署 (CI/CD) 通过 Docker 加速应用管道自动化和应用部署。
- 微服务 加速应用架构现代化进程。
- IT 基础设施优化 充分利用基础设施，节省资金

# 容器化技术VS虚拟机
- 传统虚拟机（比如，vmware，virtualbox）需要占用大量硬件资源
- 虚拟启动时间慢
- 架构图对比
    - ![传统虚拟机](https://raw.githubusercontent.com/Danielyan86/xiaoshujiang_images/master/小书匠/1593695963154.png)
    - ![docker](https://raw.githubusercontent.com/Danielyan86/xiaoshujiang_images/master/小书匠/1593696201008.png)

# 什么是docker？
- Docker是一个开源的引擎，可以轻松的为各种应用创建一个轻量级的、可移植的、自给自足的容器。
- 容器化技术的一种实现
- 目前最流行的容器化技术
- 初学者可以理解docker是个轻量级虚拟机，但实际上和虚拟机实现原理不一样