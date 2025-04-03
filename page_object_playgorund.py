# Base +. Blueprint
# Page : Click / Input text / find element, etc.,

class Page:
    def click(self ):
        print('Clicking ....')

    def find_element(self):
        print('Searching for element ....')

    def verify_text(self, actual_text):
        print(f'Verify {actual_text} ....')

class MainPage(Page):
    def open_main(self):
        print('Opening main page ....')

class LoginPage(Page):
    def login(self):
        print('Login')

login_page = LoginPage()
login_page.login()
login_page.click()
login_page.find_element()
