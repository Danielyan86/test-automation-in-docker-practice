# 此文件夹用于UI自动化测试例子演示
## 环境准备
- 基础镜像介绍 https://github.com/elgalu/docker-selenium
- 编译镜像  
```docker
docker build -t automation-test .
```
## UI自动化例子
- 打开浏览器输入bing.com
- 搜索框输入test并回车

## 运行方式
### 1. 脚本运行在本地，selenium运行环境也在本地
```shell script
python BingAutomationTest_local.py
```
### 2. 通过selenium-grid方式在容器里面运行。脚本运行在本地，selenium运行环境环境在容器里。
```shell script
# 启动容器
python BingAutomationTest_container_2.py
```
### 3. 脚本和selenium都在容器里面运行。
```shell script
sh run_script_in_container_2.sh
```

## 多容器化运行
- 启动两个带有UI自动化测试的容器 sh start_2_containers.sh
```shell script
sh start_2_containers.sh 
Total reclaimed space: 0B
5edbbdd79a9aad84da8f9273b12439d3466aebc128de41616a29c405a19ebfa5
b5196eecacf8180c22f7fad8faf12d1e3011ce2ba2b1866a413874e0b6f530c4
```
- 确认两个容器已经启动
- 在两个容器里面分别运行脚本
```shell script
python BingAutomationTest_container.py
python BingAutomationTest_container_2.py
```


