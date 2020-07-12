# 环境准备
### 安装 Jenkins
- https://www.jenkins.io/download/
### 启动Jenkins
#### 初始化密码位置
 - /Users/admin/.jenkins/secrets/initialAdminPassword
#### 启动命令
```shell script
jenkins-lts
``` 
#### 访问Jenkins
- 127.0.0.1:8080

# Jenkins pipeline demo
### 步骤
- 创建pipeline任务，粘贴此文件夹下面的Jenkinsfile到script里面
- 运行任务
- 访问http://127.0.0.1:4000/
- 修改FlaskAppDemo代码并推送
- 再次运行任务
- 查看更新代码效果
### jenkinfile定义内容
- 拉取代码
- 编译镜像
- 停止容器
- 启动容器


