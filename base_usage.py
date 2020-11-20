from selenium import webdriver
import time

def open_html(driver):
    driver.get('https://github.com/sing-zzj?tab=repositories')  # 打开一个网页
    driver.maximize_window()  # 窗口最大化
    print(driver.page_source) # 打印网页源码
    time.sleep(5)
    driver.quit()  # 关闭打开的网页

# 在网页内截图
def screen(driver):
    driver.get('https://github.com/sing-zzj?tab=repositories')
    driver.maximize_window()

    driver.save_screenshot('github.png')  # 可视网页截图

    element = driver.find_element_by_xpath('//div[@class="position-relative d-inline-block col-2 col-md-12 mr-3 mr-md-0 flex-shrink-0"]/a/img')
    element.screenshot('picture.png')     # 特定元素截图

    driver.quit()

if __name__ == '__main__':
    Chrome_driver = webdriver.Chrome()
    #open_html(Chrome_driver)
    #screen(Chrome_driver)
