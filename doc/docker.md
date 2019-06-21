# Docker
在没有远程服务器的情况下，可以将项目打包后部署到docker上面。
### 1、安装包含python3的ubuntu镜像
docker_init里面包含一个别人制作好的Dockerfile，及制作脚本，直接运行make image，可以生成一个docker image
#### 1.1 制作镜像
进入docker_init目录，执行make image，等待镜像制作完成
#### 1.2 运行容器
```.env
docker run -itd -v local_dir:docker_dir -n network -p local_port:docker_port --name container_name image_name:tag
```
-itd:   i：可交互
        t：终端
        d：是否后台执行
        
-n：绑定网络，如果启动容器时没有绑定，可以后期通过docker network命令进行绑定

-v：将本地目录映射到docker里面的目录

-p：将本地端口映射到docker端口

--name：给运行的容器命名

image_name:tag 运行容器使用的image，如果image有重名的，需要指定tag