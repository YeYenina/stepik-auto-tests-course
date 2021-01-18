from selenium import webdriver
import time

# Открыть страницу
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

time.sleep(1)
# Нажать на кнопку "Verify"
button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

# Проверить, что появилась надпись "Verification was successful!"
assert "successful" in message.text



