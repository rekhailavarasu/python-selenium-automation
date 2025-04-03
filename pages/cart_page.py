from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    cart_empty_msg = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    def verify_cart_empty(self):
        expected_text = 'Your cart is empty'
        actual_text = self.find_element(*self.cart_empty_msg).text
        assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'