# 项目介绍
### 此项目启动后中有三个容器，分别在compose模板中定义了启动和方式。
- web-app 被测试项目，模式实战中的待测项目
- UI_environment 用来启动浏览器的UI容器
- automation_env 用来跑自动化脚本的容器，因为UI_environment这个服务启动需要点时间，因此调用一个wait的shell脚本来等待UI_environment环境的启动
### 脚本内容
- 打开浏览器 输入
### 容器启动中等待另外一个服务启动方法
- https://docs.docker.com/compose/startup-order/