## 容器生命周期管理
- run : 创建一个新的容器并运行一个命令
- start/stop/restart : 启动/停止/重启一个容器
- kill : 杀掉一个运行中的容器。
- rm : 删除一个或多个容器。
- pause/unpause : 暂停容器中所有的进程。
- create : 创建一个新的容器但不启动它
- exec : 在运行的容器中执行命令.e.g. docker exec -i -t  mynginx /bin/bash
## 容器操作
- ps : 列出容器.
- inspect
- top
- attach : 连接到正在运行中的容器。
- events
- logs
- wait
- export
- port
## 容器rootfs命令
- commit
- cp
- diff
## 镜像仓库
- login
- pull
- push
- search
## 本地镜像管理
- images :  列出本地镜像。
- rmi : 删除本地一个或多少镜像。
- tag
- build : 命令用于使用 Dockerfile 创建镜像。
- history
- save : 将指定镜像保存成 tar 归档文件。
- load : 导入使用 docker save 命令导出的镜像。
- import
## info|version
- info
- version
