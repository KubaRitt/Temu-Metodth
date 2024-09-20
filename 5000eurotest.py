from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

# Open the website (replace with the actual website)
driver.get("https://www.instagram.com/accounts/emailsignup/")

# Set up an explicit wait (e.g., 10 seconds timeout)
wait = WebDriverWait(driver, 10)

# Locate the parent element with multiple classes
parent_element = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "._a9--._ap36._a9_0")
))

first_button= driver.find_element(By.CSS_SELECTOR, "._a9--._ap36._a9_0")
print("clicking")
# Click the button
first_button.click()

time.sleep(30)

# Close the browser after a short delay
driver.quit()
