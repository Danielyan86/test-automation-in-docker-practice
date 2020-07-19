import time

from selenium import webdriver

# 在集群内一个容器访问另外一个容器

url = "web-app:80"
selenium_grid_url = "http://127.0.0.1:4444/wd/hub"
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
d = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities=capabilities)

d.get(url)
time.sleep(6)
d.close()
d.quit()