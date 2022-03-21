from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    s_num1 = browser.find_element_by_id('num1')
    num1 = s_num1.text
    s_num2 = browser.find_element_by_id('num2')
    num2 = s_num2.text
    x = str(int(num1) + int(num2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(x)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(5)
    browser.quit()
