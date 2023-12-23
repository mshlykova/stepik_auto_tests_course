from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Define formula
    a_element = browser.find_element(By.ID, "num1")
    a = a_element.text

    b_element = browser.find_element(By.ID, "num2")
    b = b_element.text

    x = int(a) + int(b)
    print(x)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(x))

    # Submit form
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()