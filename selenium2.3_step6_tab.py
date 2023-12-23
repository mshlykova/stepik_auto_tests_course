from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Click button
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    #Switch to new tab
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Define formula
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Calculate formula
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Enter calculated value
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # Submit form
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла