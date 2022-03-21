from selenium import webdriver
import time
from math import sin, log

def calc(x):
    return log(abs(12*sin(x)))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element_by_class_name("trollface")
    button.click()
    new = browser.window_handles[1]
    browser.switch_to.window(new)
    time.sleep(1)
    value = browser.find_element_by_id('input_value')
    x = int(value.text)
    y = str(calc(x))
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_tag_name('button').click()
    print(browser.switch_to.alert.text)


finally:
    time.sleep(7)
    browser.quit()

