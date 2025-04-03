from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
import time

# get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()


search_field = (By.ID, 'search')
search_button = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
search_result = (By.XPATH, "//div[@data-test='lp-resultsCount']")
select_product = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
Add_cart = (By.CSS_SELECTOR, '[data-test="content-wrapper"] [id*="addToCartButton"]')


# open the url

@given('Open target main page')
def open_main_page(context):
    context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()
    #context.driver.wait = WebDriverWait(context.driver, 10)
    context.driver.wait.until(
        EC.element_to_be_clickable(search_field),
        message='Search field not clickable'
    )
# @when('Search for {coffee}')
# def search_product(context, coffee):
#     context.driver.find_element(*search_field).send_keys(coffee)
#     context.driver.find_element(*search_button).click()
#     sleep(3)
#
@then('Verify the results shown is for coffee')
def verify_results_shown(context):
    actual_results = context.driver.find_element(*search_result).text
    expected_results = 'coffee'
    assert expected_results in actual_results, f'Error, Text {expected_results} not found in {actual_results}'

@then('Verify the results shown is for {expected_results}')
def verify_results_shown(context, expected_results):
    context.app.search_results.verify_search_results(expected_results)

#     actual_results = context.driver.find_element(*search_result).text
#     expected_results = 'tea'
#     assert expected_results in actual_results, f'Error, Text {expected_results} not found in {actual_results}'
#     sleep(3)
#
# @then('Verify correct search results shown for {expected_result}')
# def verify_results_shown(context, expected_result):
#     actual_results = context.driver.find_element(*search_result).text
#     assert expected_result in actual_results, f'Error, Text {expected_result} not found in {actual_results}'

@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search()
    # context.driver.find_element(*search_field).send_keys(search_word)
    # context.driver.find_element(*search_button).click()
    # context.driver.wait.until(
    #     EC.presence_of_element_located(search_result),  # Wait for the results to load
    #     message="Search results did not load properly"
    # )



@when('Select an item to Add to cart')
def select_item(context):
    attempts = 0
    while attempts < 3:
        try:
            # Wait until the "Add to Cart" button is clickable
            add_to_cart_button = context.driver.wait.until(
                EC.element_to_be_clickable(select_product)
            )

            # Scroll the element into view
            context.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)

            # Click the "Add to Cart" button
            add_to_cart_button.click()
            break
        except ElementClickInterceptedException:
            print("Element is blocked, retrying...")
            time.sleep(2)  # Wait a bit before retrying
            attempts += 1

@when('Continue to click on Add to cart')
def continue_to_cart(context):
    attempts = 0
    while attempts < 3:
        try:
            # Wait until the "Add to Cart" button is clickable
            add_to_cart_button = WebDriverWait(context.driver, 10).until(
                EC.element_to_be_clickable(Add_cart)
            )

            # Scroll the element into view to ensure it's not outside of the viewport
            context.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)

            # Click the "Add to Cart" button
            add_to_cart_button.click()
            print("Clicked on Add to Cart")
            break
        except ElementClickInterceptedException:
            print("Element is blocked, retrying...")
            time.sleep(2)  # Wait a bit before retrying
            attempts += 1
        except TimeoutException:
            print("Timed out waiting for Add to Cart button to be clickable.")
            break
        except Exception as e:
            print(f"Error during clicking: {e}")
            break

    # Returning to the Target homepage
    context.driver.get('https://www.target.com/')
    context.driver.wait.until(
        EC.element_to_be_clickable(search_field),
        message='Search field not clickable'
    )
