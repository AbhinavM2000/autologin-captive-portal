from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_to_captive_portal():
    url = 'your captive portal ip here'
    username = 'your username here'
    password = 'your password here'

    driver = webdriver.Chrome()  # You'll need to have ChromeDriver installed
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    username_field = driver.find_element(By.ID, 'username') #modify as per the captive portal login page structure
    password_field = driver.find_element(By.ID, 'password') #modify as per the captive portal login page structure
    login_button = driver.find_element(By.ID, 'loginbutton') #modify as per the captive portal login page structure

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    # Allow some time for the login process to complete
    time.sleep(5)

    driver.quit()

while True:
    login_to_captive_portal()
    time.sleep(1* 60 * 60)  # Sleep for 2 hours (2 * 60 * 60 seconds)
