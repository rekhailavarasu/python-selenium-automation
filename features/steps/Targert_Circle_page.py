from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

Target_circle = (By.ID, 'utilityNav-circle')
Header_links = (By.CSS_SELECTOR, '[data-test="@web/slingshot-components/CellsComponent/Link"]')
#Header_links = (By.XPATH, "//a[data-test='@web/slingshot-components/CellsComponent/Link']")

# @given ('Open Target Page')
# def open_target_page(context):
#     context.driver.get("https://www.target.com/")
#     sleep(1)

@when ('Navigate to Target circle')
def navigate_target_circle(context):
    context.driver.find_element(*Target_circle).click()
    sleep(6)

@then ('Verify at least 10 {link_amount} benefits links shown inside Target circle')
def verify_all_links(context, link_amount):
    link_amount = 10
    links = context.driver.find_elements(*Header_links)
    print(len(links))
    assert len(links) >= link_amount, f'Error, {link_amount} links not found in {len(links)}'
