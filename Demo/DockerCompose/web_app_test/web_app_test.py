import time

from selenium import webdriver

# 在集群内一个容器访问另外一个容器

url = "web-app:80"
host = "UI_environment"
selenium_grid_url = f"http://{host}:24444/wd/hub"
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
d = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities=capabilities)

d.get(url)
time.sleep(20)
d.close()
d.quit()
