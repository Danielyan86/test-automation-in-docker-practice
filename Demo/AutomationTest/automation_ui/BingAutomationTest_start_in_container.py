import logging
import time

from selenium import webdriver


def run_UI_test_in_docker_env():
    # selenium grid方式远程运行
    current_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    logging.basicConfig(filename="./selenium_deb_log_{0}".format(current_time), level=logging.DEBUG)

    selenium_grid_url = "http://127.0.0.1:24444/wd/hub"
    capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    d = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities=capabilities)

    # 设置超时
    d.set_page_load_timeout(20)
    d.set_script_timeout(20)

    url = "http://www.bing.com"
    text_box_id = "sb_form_q"
    # 输入URL
    d.get(url)
    # 搜索框输入test
    try:
        d.find_element_by_id(text_box_id).send_keys("test\n")
    except Exception as e:
        print(e)
    finally:
        time.sleep(10)
        d.close()
        d.quit()


if __name__ == '__main__':
    run_UI_test_in_docker_env()
