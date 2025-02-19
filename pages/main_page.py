from .base_page import BasePage
from .locators import MainPageLocators as mpl

class MainPage (BasePage):
    def check_b4ttons(self):
        for button in mpl.BUTTONS_BOOKS:
            button = self.is_present(*button)
            assert button != False, 'Error of Button'
        
    def click_button(self, index):
        self.is_present(*mpl.BUTTONS_BOOKS[index]).click()
        
    def check_messsage(self):
        message = self.is_present(*mpl.MESSAGE_REGISTER)
        assert message != False, 'Error of Message'
        




