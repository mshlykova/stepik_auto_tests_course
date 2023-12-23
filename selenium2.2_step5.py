from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

# Enter calculated value
input1 = browser.find_element(By.ID, "answer")
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

time.sleep(10)