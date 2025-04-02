# Base +. Blueprint
# Page : Click / Input text / find element, etc.,

class Page:
    def click(self ):
        print('Clicking ....')

    def find_element(self):
        print('Searching for element ....')

    def verify_text(self, actual_text):
        print(f'Verify {actual_text} ....')

class MainPage: