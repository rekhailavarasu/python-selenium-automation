from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

search_field = (By.ID, 'search')
search_button = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
search_result = (By.XPATH, "//div[@data-test='lp-resultsCount']")
select_product = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
Add_cart = (By.CSS_SELECTOR, '[data-test="content-wrapper"] [id*="addToCartButton"]')
Added_to_cart = (By.CSS_SELECTOR, '[class="h-text-lg"]')

# open the url

@given('Open target page')
def open_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(2)

@when('Search for {coffee}')
def search_product(context, coffee):
    context.driver.find_element(*search_field).send_keys(coffee)
    context.driver.find_element(*search_button).click()
    sleep(3)

@then('Verify the results shown is for coffee')
def verify_results_shown(context):
    actual_results = context.driver.find_element(*search_result).text
    expected_results = 'coffee'
    assert expected_results in actual_results, f'Error, Text {expected_results} not found in {actual_results}'

@then('Verify the results shown is for tea')
def verify_results_shown(context):
    actual_results = context.driver.find_element(*search_result).text
    expected_results = 'tea'
    assert expected_results in actual_results, f'Error, Text {expected_results} not found in {actual_results}'
    sleep(3)

@then('Verify correct search results shown for {expected_result}')
def verify_results_shown(context, expected_result):
    actual_results = context.driver.find_element(*search_result).text
    assert expected_result in actual_results, f'Error, Text {expected_result} not found in {actual_results}'

@when('Select an item to Add to cart')
def select_item(context):
    context.driver.find_element(*select_product).click()
    sleep(4)

@when('Continue to click on Add to cart')
def continue_to_cart(context):
    context.driver.find_element(*Add_cart).click()
    sleep(4)

@then('Verify the message "Added to cart"')
def message(context):
    context.driver.find_elements(*Added_to_cart)
    sleep(4)

driver.quit()
