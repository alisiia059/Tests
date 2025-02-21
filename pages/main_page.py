from .base_page import BasePage
from .locators import MainPageLocators as mpl

class MainPage (BasePage):
    def check_b4ttons(self):
        """
        Verifies that all the buttons in the list (of 5 first books) are present on the page.

        Args:
            None

        Example:
            page.check_b4ttons()
        """
        for button in mpl.BUTTONS_BOOKS:
            button = self.is_present(*button)
            assert button != False, 'Error of Button'
        
    def click_button(self, index):
        """
        Clicks the button at the specified index in the book list.

        Args:
            index (int): The index of the button to be clicked.

        Example:
            page.click_button(0)  # Clicks the first button
        """
        self.is_present(*mpl.BUTTONS_BOOKS[index]).click()
        
    def check_messsage(self):
        """
        Verifies that the registration message is present on the page.

        Args:
            None

        Example:
            page.check_messsage()
        """

        message = self.is_present(*mpl.MESSAGE_REGISTER)
        assert message != False, 'Error of Message'
        




