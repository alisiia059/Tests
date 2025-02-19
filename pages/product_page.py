from .base_page import BasePage
from .locators import ProductPageLocators as ppl

class ProductPage (BasePage):

    def write_review_buttton(self):
        button = self.is_present(*ppl.BUTTON_WRITE_REVIEW)
        assert button != False, 'Error of Button'
        button.click()

    def add_busket_buttton(self):
        button = self.is_present(*ppl.BUTTON_ADD_BUSKET)
        assert button != False, 'Error of Button'
        button.click()

    def title_field(self, title):
        field = self.is_present(*ppl.TITLE_FIELD)
        assert field != False, 'Error of InputField'
        field.send_keys(title)
    
    def body_field(self, body):
        field = self.is_present(*ppl.BODY_FIELD)
        assert field != False, 'Error of InputField'
        field.send_keys(body)

    def name_field(self, name):
        field = self.is_present(*ppl.NAME_FIELD)
        assert field != False, 'Error of InputField'
        field.send_keys(name)
    
    def email_field(self, email):
        field = self.is_present(*ppl.EMAIL_FIELD)
        assert field != False, 'Error of InputField'
        field.send_keys(email)

    def save_review_buttton(self):
        button = self.is_present(*ppl.BUTTON_SAVE_REVIEW)
        assert button != False, 'Error of Button'
        button.click()
    
    def add_book_busket(self):
        self.add_busket_buttton()
        name = self.is_present(*ppl.PRODUCT_NAME)
        price = self.is_present(*ppl.PRODUCT_PRICE)
        name_site = self.is_present(*ppl.AFTER_ADDING_NAME)
        price_site = self.is_present(*ppl.AFTER_ADDING_PRICE)
        print(price.text, price_site.text) #токсик
        assert  name.text == name_site.text
        assert price.text == price_site.text

    def write_review(self, title, body, name, email):
        self.write_review_buttton()
        self.title_field(title)
        self.body_field(body)
        self.name_field(name)
        self.email_field(email)
        self.save_review_buttton()


        