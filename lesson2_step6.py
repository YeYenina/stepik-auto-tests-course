from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) 

try:
    #Открыть страницу
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    #Считать значение для переменной x
    x = browser.find_element_by_id("input_value")
    x_1 = x.text

    #Посчитать математическую функцию от x
    y = calc(x_1)

    #Ввести ответ в текстовое поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()