from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@given('Open target main page')
def open_target_main(context):
    driver_path = ChromeDriverManager().install()
    context.driver = webdriver.Chrome(service=Service(driver_path))
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.get('https://www.target.com/')
@when('Click on cart icon')
def cart_icon(context):
    wait = WebDriverWait(context.driver, 10)  # Wait up to 10 seconds
    cart_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='@web/CartIcon']")))
    cart_element.click()


@then("Verify  'Your cart is empty' message is shown")
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'

