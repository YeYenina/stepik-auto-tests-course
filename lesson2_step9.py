from selenium import webdriver
import time

# Открыть страницу
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")

# Нажать на кнопку "Verify"
button = browser.find_element_by_id("button")
button.click()
