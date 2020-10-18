#!/usr/bin/env bash

docker container stop $(docker container list -q)
docker container prune -f