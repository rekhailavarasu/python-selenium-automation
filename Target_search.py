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

# open the url
driver.get('https://www.target.com/')

# Click "Sign in button"
Sign_in = driver.find_element(By.XPATH, "//span[@class='sc-43f80224-3 fBDEOp h-margin-r-x3']")
Sign_in.click()

sleep(5)

# Click "Sign in button" from side navigation
click_sign_in = driver.find_element(By.XPATH, "//button[@type='button']")
click_sign_in.click()

sleep(5)




