# 环境安装和镜像准备
## docker 相关安装
- 推荐学习文档 https://yeasy.gitbooks.io/docker_practice/
- 官网安装文档 https://docs.docker.com/install/
- 中文安装文档 https://yeasy.gitbooks.io/docker_practice/content/install/ 
- docker-compose 安装文档 https://docs.docker.com/compose/install/
- Win10用户需要使用使用正版旗舰版。并开启hyper-V服务和BIOS虚拟化设置。https://jingyan.baidu.com/article/ac6a9a5e1f164a2b653eac33.html
- Docker 安装包建议从官网下载免费社区版
- 无法直接安装在本机的同学，比如win7。可以尝试使用virtualbox安装Ubuntu虚拟机，在虚拟机里面再安装docker。也可以上网搜索其他方式。建议直接安装在本机上。
- 把docker安装在windows的virtualbox里面的，本地默认访问*IP为192.168.99.100
## 镜像准备
- 配置阿里云镜像加速器
  - 注册阿里云账号
  - 参考文章 https://yq.aliyun.com/articles/29941
- 安装好docker的同学，请提前拉取一下镜像到本地。
  - Docker pull ubuntu:16.04
  - Docker pull elgalu/selenium
  - docker pull oscarcommerce/django-oscar-sandbox
  
## 其他工具
- VNC客户端安装

# 练习部分
所有演示文件和代码放在DockerDemo下面
