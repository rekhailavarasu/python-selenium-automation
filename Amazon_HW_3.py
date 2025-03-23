from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Verify "amazon logo" by CSS class
driver.find_element(By.CSS_SELECTOR, '.a-icon')
# Verify "Create account" heading by CSS class
driver.find_element(By.CSS_SELECTOR, '.a-spacing-small')
# Verify "Your first and last name field" By CSS ID
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')
# Verify "Mobile number or email" field By CSS ID
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')
# Verify "Password" field By CSS ID
driver.find_element(By.CSS_SELECTOR, 'input#ap_password')
# Verify "Password must be at least 6 characters" field By CSS class
driver.find_element(By.CSS_SELECTOR, '.a-alert-content')
# Verify "Re-enter Password" field By CSS ID
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')
# Verify "Continue" button By CSS class
driver.find_element(By.CSS_SELECTOR, '.a-button-input')
# Verify "Condition of Use" link By CSS ID and class
driver.find_element(By.CSS_SELECTOR, '#legalTextRow [href*="ap_register_notification_condition_of_use"]')
# Verify "Privacy notice" link By CSS class
driver.find_element(By.CSS_SELECTOR, '#legalTextRow [href*="ap_register_notification_privacy_notice"]')
# Verify "Sign in" link By CSS class
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')