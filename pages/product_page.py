from .base_page import BasePage
from .locators import ProductPageLocators as ppl

class ProductPage (BasePage):

    def write_review_buttton(self):
        """
        Clicks the 'Write Review' button on the product page.

        Args:
            None

        Example:
            page.write_review_buttton()
        """
        button = self.is_present(*ppl.BUTTON_WRITE_REVIEW)
        assert button != False, 'Error of Button'
        button.click()

    def add_busket_buttton(self):
        """
        Clicks the 'Add to Basket' button to add the product to the basket.

        Args:
            None

        Example:
            page.add_busket_buttton()
        """
        button = self.is_present(*ppl.BUTTON_ADD_BUSKET)
        assert button != False, 'Error of Button'
        button.click()

    def title_field(self, title):
        """
        Inputs the review title into the review title field.

        Args:
            title (str): The title of the review.

        Example:
            page.title_field("Great Product!")
        """
        field = self.is_present(*ppl.TITLE_FIELD)
        assert field != False, 'Error of InputField'
        field.send_keys(title)
    
    def body_field(self, body):
        """
        Inputs the review body into the review body field.

        Args:
            body (str): The content of the review.

        Example:
            page.body_field("This product is fantastic!")
        """
        field = self.is_present(*ppl.BODY_FIELD)
        assert field != False, 'Error of InputField'
        field.send_keys(body)

    def name_field(self, name):
        """
        Inputs the name into the review name field.

        Args:
            name (str): The name of the person writing the review.

        Example:
            page.name_field("Alisiia")
        """
        field = self.is_present(*ppl.NAME_FIELD)
        assert field != False, 'Error of InputField'
        field.send_keys(name)
    
    def email_field(self, email):
        """
        Inputs the email into the review email field.

        Args:
            email (str): The email of the person writing the review.

        Example:
            page.email_field("johndoe@example.com")
        """
        field = self.is_present(*ppl.EMAIL_FIELD)
        assert field != False, 'Error of InputField'
        field.send_keys(email)

    def save_review_buttton(self):
        """
        Clicks the 'Save Review' button to submit the written review.

        Args:
            None

        Example:
            page.save_review_buttton()
        """
        button = self.is_present(*ppl.BUTTON_SAVE_REVIEW)
        assert button != False, 'Error of Button'
        button.click()
    
    def add_book_busket(self):
        """
        Adds the product to the basket, and verifies that the product's name 
        and price match between the product page and the basket page.

        Args:
            None

        Example:
            page.add_book_busket()
        """
        self.add_busket_buttton()
        name = self.is_present(*ppl.PRODUCT_NAME)
        price = self.is_present(*ppl.PRODUCT_PRICE)
        name_site = self.is_present(*ppl.AFTER_ADDING_NAME)
        price_site = self.is_present(*ppl.AFTER_ADDING_PRICE)

        assert  name.text == name_site.text
        assert price.text == price_site.text

    def write_review(self, title, body, name, email):
        """
        Writes a product review by filling in the title, body, name, and email, 
        then submits the review.

        Args:
            title (str): The title of the review.
            body (str): The content of the review.
            name (str): The name of the person writing the review.
            email (str): The email of the person writing the review.

        Example:
            page.write_review("Great Product!", "This product is amazing!", "John Doe", "johndoe@example.com")
        """
        self.write_review_buttton()
        self.title_field(title)
        self.body_field(body)
        self.name_field(name)
        self.email_field(email)
        self.save_review_buttton()


        