from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
SHOE_CLR_OPTION = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li class")
CLR_SELECTED = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]

    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


@then('Verify user can click through shoe colors')
def verify_colors(context):
    colors_shown = ['black', 'blue', 'coral', 'leopard']
    actual = []

    shoe_colors = context.driver.find_elements(*SHOE_CLR_OPTION)

    for Shoecolor in shoe_colors:
        Shoecolor.click()

        clr_selected = context.driver.find_element(*CLR_SELECTED).text  # 'Color\nBlack'
        print('Current color', clr_selected)

        clr_selected = clr_selected.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual.append(clr_selected)
        print(actual)

        assert colors_shown == actual, f'Expected {colors_shown} did not match actual {actual}'