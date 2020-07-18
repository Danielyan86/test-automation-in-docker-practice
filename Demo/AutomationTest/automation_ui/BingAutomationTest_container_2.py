import logging
import time

from selenium import webdriver

timeout_number = 25


def run_UI_test_in_docker_env(selenium_grid_url=None):
    # selenium grid方式远程运行
    current_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    logging.basicConfig(filename="./selenium_deb_log_{0}".format(current_time), level=logging.DEBUG)

    capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    d = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities=capabilities)

    # 设置超时
    d.set_page_load_timeout(timeout_number)
    d.set_script_timeout(timeout_number)

    url = "http://www.bing.com"
    text_box_id = "sb_form_q"

    try:
        d.get(url)  # 输入URL
        d.find_element_by_id(text_box_id).send_keys("test\n")  # 搜索框输入test
    except Exception as e:
        print(e)
    finally:
        time.sleep(20)
        d.close()
        d.quit()


if __name__ == '__main__':
    # 运行此脚本之前需要一个已经启动起来的容器
    # docker run -d --rm -p 5906:25900 -p 4446:24444 --name automation-container_2  -e SCREEN_WIDTH=1024 -e SCREEN_HEIGHT=768 automation-test:latest
    # 此脚本用于本地执行，方便调试使用
    selenium_grid_url = "http://127.0.0.1:4446/wd/hub"
    run_UI_test_in_docker_env(selenium_grid_url=selenium_grid_url)
