from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators as bpl
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__ (self, browser: Chrome, url: str):
        self.browser = browser 
        self.url = url
     
    def open (self):
        self.browser.get(self.url)
    
    def is_present (self, by, value) -> WebElement:
        try:
            item = self.browser.find_element(by, value)
            return item
        except NoSuchElementException:
            print ('No such element')
            return False
        except:
            print ('Unknown error')
            return False
    
    def input_text_search_field(self, text):
        input_field = self.is_present(*bpl.SEARCH_FIELD) #автораспаковка
        button = self.is_present(*bpl.BUTTON_SEARCH)
        assert input_field != False, 'Error of InputField'
        assert button != False, 'Error of Button'
        input_field.send_keys(text)
        button.click()
    
    def view_busket(self):
        button = self.is_present(*bpl.BUTTON_BUSKET) 
        assert button != False, 'Error of Button'
        button.click()

    def click_login(self):
        button = self.is_present(*bpl.BUTTON_LOGIN) 
        assert button != False, 'Error of Button'
        button.click()
    
    def choose_language(self, language):
        """_summary_

        Args:
            language (str): it should be code of language given as a value (en-gb, ru)
        Example:
            page.choose_language('en-gb')
        """        
        language_field = self.is_present(*bpl.CHANGE_LANGUAGE)
        button = self.is_present(*bpl.BUTTON_DO)
        assert language_field != False, 'Error of InputField'
        assert button != False, 'Error of Button'
        select_language = Select(language_field)
        select_language.select_by_value(language) 
        button.click()

    def get_current_url(self):
        return self.browser.current_url
