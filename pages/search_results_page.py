from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    search_result = (By.XPATH, "//div[@data-test='lp-resultsCount']")

    def verify_search_results(self, expected_results):
        actual_results = self.find_element(*self.search_result).text
        assert expected_results in actual_results, f'Error. Text {expected_results} not in {actual_results}'
        # print(self.search_result)
        #
        # try:
        #     actual_results = self.find_element(self.search_result).text
        #     print(actual_results)
        # except Exception as e:
        #     print(e)


