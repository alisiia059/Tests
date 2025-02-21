from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators as bpl
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__ (self, browser: Chrome, url: str):
        """
        _summary_

        Initializes the BasePage object with the given browser and URL.

        Args:
            browser (Chrome): Selenium browser instance (e.g., Chrome).
            url (str): URL of the page to be loaded.
        
        Example:
            page = BasePage(browser, "http://example.com")
        """
        self.browser = browser 
        self.url = url
     
    def open (self):
        """
        _summary_

        Opens the page using the URL provided during initialization.

        Args:
            None
        
        Example:
            page.open()
        """
        self.browser.get(self.url)
    
    def is_present (self, by, value) -> WebElement:
        """
        _summary_

        Checks if an element is present on the page by a given locator 
        (by, value) and returns the element if found.

        Args:
            by: Locator strategy (e.g., By.ID, By.NAME, By.XPATH, BY.CSS_SELECTOR, By.CLASS_NAME).
            value: The value for the locator (e.g., element_id or element_class).
        
        Returns:
            WebElement: If the element is found, returns the WebElement.
            False: If the element is not found, returns the FALSE.
        
        Example:
            element = page.is_present(By.ID, "submit-button")
        """
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
        """
        _summary_

        Inputs the provided text into a search field and clicks the search button.

        Args:
            text (str): The text to be entered into the search field.
        
        Example:
            page.input_text_search_field("Book")
        """
        input_field = self.is_present(*bpl.SEARCH_FIELD) #автораспаковка
        button = self.is_present(*bpl.BUTTON_SEARCH)
        assert input_field != False, 'Error of InputField'
        assert button != False, 'Error of Button'
        input_field.send_keys(text)
        button.click()
    
    def view_busket(self):
        """
        _summary_

        Clicks the 'View Basket' button to open the bucket page.

        Args:
            None
        
        Example:
            page.view_busket()
        """
        button = self.is_present(*bpl.BUTTON_BUSKET) 
        assert button != False, 'Error of Button'
        button.click()

    def click_login(self):
        """
        _summary_

        Clicks the 'Login' button to navigate to the login page.

        Args:
            None
        
        Example:
            page.click_login()
        """
        button = self.is_present(*bpl.BUTTON_LOGIN) 
        assert button != False, 'Error of Button'
        button.click()
    
    def choose_language(self, language):
        """
        _summary_

        Selects the specified language from a dropdown and applies the language change.

        Args:
            language (str): Language code to select (e.g., 'en-gb', 'ru').
        
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
        """
        _summary_

        Returns the current URL of the page.

        Args:
            None
        
        Returns:
            str: The current URL as a string.
        
        Example:
            current_url = page.get_current_url()
        """
        return self.browser.current_url
