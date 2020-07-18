From ubuntu:16.04
# entrypoint 允许在docker run时候加参数 例如 docker run entrypoint -l
ENTRYPOINT ["ls"]