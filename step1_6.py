from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем обязательные поля
    field_first_name = browser.find_element_by_css_selector('input.first[required]')
    field_first_name.send_keys('Test1')
    field_last_name = browser.find_element_by_css_selector('.second[required]')
    field_last_name.send_keys('Test2')
    field_email = browser.find_element_by_css_selector('.third[required]')
    field_email.send_keys('Test3')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text



finally:
    time.sleep(5)
    browser.quit()

#625385404