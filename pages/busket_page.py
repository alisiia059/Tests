from .base_page import BasePage
from .locators import BusketPageLocators as bpl
from selenium.webdriver.support.ui import Select

class BusketPage (BasePage):

    def shipping_address(self):
        """
        Fills in all fields in the delivery order form with provided values and submits it.

        Args:
            None

        Example:
            page.shipping_address()
        """
        title = self.is_present(*bpl.BUTTON_TITLE) #select
        first_name = self.is_present(*bpl.BUTTON_FIRST_NAME)
        last_name = self.is_present(*bpl.BUTTON_LAST_NAME)
        line1 = self.is_present(*bpl.BUTTON_LINE1)
        line2 = self.is_present(*bpl.BUTTON_LINE2)
        line3 = self.is_present(*bpl.BUTTON_LINE3)
        city = self.is_present(*bpl.BUTTON_CITY)
        state = self.is_present(*bpl.BUTTON_STATE)
        postcode = self.is_present(*bpl.BUTTON_POSTCODE) #91701
        country = self.is_present(*bpl.BUTTON_COUNTRY) #select
        phone_number = self.is_present(*bpl.BUTTON_PHONE_NUMBER) #+421455245
        instructions = self.is_present(*bpl.BUTTON_INSTRUCTIONS)
        title = Select(title)
        country = Select(country)
        # Filling in the form
        title.select_by_value('Miss')
        first_name.send_keys('Alisiia')
        last_name.send_keys('Khaliulina')
        line1.send_keys('Moi')
        line2.send_keys('krutoy')
        line3.send_keys('address')
        city.send_keys('gorod')
        state.send_keys('netu')
        postcode.send_keys('91701')
        country.select_by_value('SK')
        phone_number.send_keys('+421455245')
        instructions.send_keys('миллиниалы')
        continue_b = self.is_present(*bpl.BUTTON_CONTINUE)
        # Click continue
        continue_b.click()

    def proceed_checkout(self):
        """
        Clicks the 'Proceed to Checkout' button to move to the next checkout step.

        Args:
            None

        Example:
            page.proceed_checkout()
        """
        button = self.is_present(*bpl.BUTTON_PROCEED_CHECKOUT)
        assert button != False, 'Error of Button'
        button.click()

    def update(self, value):
        """
        Updates the quantity of an item in the basket and clicks the 'Update' button.

        Args:
            value (str): The quantity value to update the basket item to.

        Example:
            page.update('2')
        """
        quantity = self.is_present(*bpl.BUTTON_BOOK_QUANTITY)
        update = self.is_present(*bpl.BUTTON_UPDATE)
        assert quantity != False, 'Error of Button'
        assert update != False, 'Error of Button'
        quantity.send_keys(value)
        update.click()
