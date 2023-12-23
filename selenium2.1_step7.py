from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Define formula
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Find x
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")

    # Calculate formula
    y = calc(x)

    # Enter calculated value
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Check robot's checbox
    check1 = browser.find_element(By.ID, "robotCheckbox")
    check1.click()

    #Select robot radio-button
    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()
      
    # Submit form
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()