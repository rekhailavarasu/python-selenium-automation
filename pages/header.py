from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    search_field = (By.ID, 'search')
    search_button = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")


    def search(self):
        self.input_text('tea', *self.search_field)
        self.click(*self.search_button)

    def click_cart(self):
        self.click(*self.CART_ICON)