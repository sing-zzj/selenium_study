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
 
# 实现网页滚动
def scroll(driver):
    
    """
    #滑动到页面中间处
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2)")
    time.sleep(3)

    #滑动到页面最下方
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)

    #滑动到页面最上方
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    """
    for i in range(0, 10000, 100):
        driver.execute_script('window.scrollBy(0, {})'.format(i))    # 当scrollBy 参数为负数时，意思是网页往上移动
        time.sleep(1.5)

if __name__ == '__main__':
    Chrome_driver = webdriver.Chrome()
    #open_html(Chrome_driver)
    #screen(Chrome_driver)
