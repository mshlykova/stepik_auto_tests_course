from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

# Define formula
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Calculate formula
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

# Enter calculated value
input1 = browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(y)

# Check robot's checbox
check1 = browser.find_element(By.ID, "robotCheckbox")
check1.click()

# Select robot radio-button
radio1 = browser.find_element(By.ID, "robotsRule")
radio1.click()

# Submit form
button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()