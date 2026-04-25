from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
url = "http://localhost:63342/assignment/login.html?_ijt=mr8s0diba06sffdlctmhdfcq78&_ij_reload=RELOAD_ON_SAVE"
driver.get(url)
driver.maximize_window()
time.sleep(2)
user_input = driver.find_element(By.ID, "user")
pass_input = driver.find_element(By.ID, "pass")

user_input.send_keys("test_user")
pass_input.send_keys("password123")
print("Step 1: Username and Password entered.")
time.sleep(2)

login_button = driver.find_element(By.CLASS_NAME, "login-btn")
login_button.click()
print("Step 2: Login button clicked.")
time.sleep(3)

try:
    welcome_msg = driver.find_element(By.TAG_NAME, "h1").text
    if "Welcome" in welcome_msg:
        print("Success: Automated Login Test Passed!")
except:
    print("Error: Could not verify login.")

driver.quit()