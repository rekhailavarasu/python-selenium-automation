from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@given('Open target sign in page')
def open_target_main(context):
    driver_path = ChromeDriverManager().install()
    context.driver = webdriver.Chrome(service=Service(driver_path))
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.get('https://www.target.com/')

@when('Click on sign in')
def Click_Sign_In(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()

@when('Navigate to sign in')
def Nav_Sign_In(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

# Verification
@then('Verify  Sign In form opened')
def verify_Sign_In(context):
    actual = context.driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
    expected = 'Sign into your Target account'
    assert expected == actual, f'Expected {expected} did not match actual {actual}'

