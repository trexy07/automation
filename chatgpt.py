from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the web driver executable
webdriver_path = 'path/to/your/webdriver'

options = webdriver.FirefoxOptions()
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)

browser = webdriver.Firefox(options=options)

# Open the webpage
browser.get('http://chatgpt.com')

# print(dir(browser))
# # Close the browser
# # browser.quit()
# import time
# time.sleep(10)
# button = browser.find_element(By.CLASS_NAME, 'btn-secondary')
# print(button)
# button.click()

# time.sleep(10)
# checkbox_label = browser.find_element(By.XPATH, "//label[contains(.,'Verify you are human')]")

# Find the checkbox within the label element
# checkbox = checkbox_label.find_element(By.TAG_NAME, 'input')

# Click the checkbox
# checkbox.click()

# browser.quit()
