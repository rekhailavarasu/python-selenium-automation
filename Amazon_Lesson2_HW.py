from asyncio import Condition

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open Amazon Sign - in page
driver.get("https://www.amazon.com/")

# Click on the "Sign In" link/button
sign_in_page = driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
sign_in_page.click()

# Look for Amazon logo
amazon_logo = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Observe Email field
Email_field = driver.find_element(By.ID, "ap_email")

# Observe "Continue" button
Continue_field = driver.find_element(By.ID, "continue")

# Check for "Conditions of use link"
Condition_link = driver.find_element(By.XPATH, "//a[contains(@href, 'ref=ap_signin_notification_condition_of_use')]")

# Check for "Privacy Notice link"
Privacy_Notice_link = driver.find_element(By.XPATH, "//a[contains(@href, 'ref=ap_signin_notification_privacy_notice')]")

# Check for "Need help link"
Need_help_link = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Check for "Forgot your password link"
forgot_password_link = driver.find_element(By.ID, "auth-fpp-link-bottom")

# Check for "Other issues with Sign-In link"
Other_issues = driver.find_element(By.ID, "ap-other-signin-issues-link")

# Check for "Create your Amazon account button"
Amazon_account_button = driver.find_element(By.ID, "createAccountSubmit")

sleep(2)




