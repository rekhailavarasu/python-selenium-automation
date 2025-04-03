from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @given('Open target main page')
# def open_target_main(context):
#     driver_path = ChromeDriverManager().install()
#     context.driver = webdriver.Chrome(service=Service(driver_path))
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(5)
#     context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def cart_icon(context):
    wait = WebDriverWait(context.driver, 10)  # Wait up to 10 seconds
    cart_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='@web/CartIcon']")))
    cart_element.click()

CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
Add_cart = (By.CSS_SELECTOR, '[data-test="content-wrapper"] [id*="addToCartButton"]')
HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
#CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
#search_result = (By.XPATH, "//div[@data-test='lp-resultsCount']")
#search_field = (By.ID, 'search')
#search_button = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

# @when('Search for {search_word}')
# def search_product(context, search_word):
#     context.driver.find_element(*search_field).send_keys(search_word)
#     context.driver.find_element(*search_button).click()
#     context.driver.wait.until(
#         EC.presence_of_element_located(search_result),  # Wait for the results to load
#         message="Search results did not load properly"

@then('Click on Add to Cart button')
def click_cart(context):
    context.app.header.click_cart()
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(CART_ICON)
    # ).click()

@then('Store product name')
def store_product_name(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not visible'
    )
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored: ', context.product_name)

@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has correct product')
def verify_product_name(context):
    # context.product_name => stored before
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    print('Name in cart: ', product_name_in_cart)
    assert context.product_name[:20] == product_name_in_cart[:20], \
        f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'


@then('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(Add_cart)
    ).click()  # Click on the "Add to Cart" button from the side navigation
    #sleep(5)
@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"

@then('Verify at least 1 link shown')
def verify_1_header_link_shown(context):
    link = context.driver.find_element(*HEADER_LINKS)
    print(link)

@then('Verify {link_amount} links shown')
def verify_all_header_links_shown(context, link_amount):
    link_amount = int(link_amount)  # "6" => int 6
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}'


@then("Verify  'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()

    # actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    # expected_text = 'Your cart is empty'
    # assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'

@then('Verify correct search results shown for {expected_result}')
def verify_results_shown(context, expected_result):
    context.app.search_results_page.verify_search_results()


    # try:
    #     actual_results_text = context.driver.find_element(*search_result).text
    #     print(f"Actual search results: {actual_results_text}")
    #
    #     # Clean the result text to get just the number (if it's in a format like "4,316 results")
    #     actual_results = ''.join([char for char in actual_results_text if char.isdigit()])
    #
    #     print(f"Actual results (numeric): {actual_results}")
    #
    #     # Check if the expected result matches the actual results
    #     assert expected_result in actual_results, f'Error, Text "{expected_result}" not found in "{actual_results_text}"'
    # except Exception as e:
    #     print(f"Error verifying results: {e}")
    #     raise
