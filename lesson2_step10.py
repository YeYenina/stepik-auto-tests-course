from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    # Нажать на кнопку "Book"
    button = WebDriverWait(browser, 12).until(
	        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)
    button = browser.find_element_by_id("book")
    button.click()

    # Проскролит страницу
    browser.execute_script("window.scrollBy(0, 100);")

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    # Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
    x_1 = browser.find_element_by_id("input_value")
    x = x_1.text

    #Посчитать математическую функцию от x
    y = calc(x)

    #Ввести ответ в текстовое поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Нажать кнопку "Submit"
    button1 = browser.find_element_by_id("solve")
    button1.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()