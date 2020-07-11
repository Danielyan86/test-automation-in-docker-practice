#!/usr/bin/env bash
set -e
docker container prune -f
docker run -d --rm -p 5906:25900 -p 4446:24444 --name automation-container_2 -v "$(pwd)":/home/seluser/automation -e SCREEN_WIDTH=1024 -e SCREEN_HEIGHT=768 automation-test:latest
sleep 20
docker exec automation-container_2 python automation/BingAutomationTest_start_in_container.py
docker container stop automation-container_2
