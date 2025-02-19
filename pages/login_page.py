from .base_page import BasePage
from .locators import LogInLocators as lil

class LogInPage (BasePage):
    def login_email_field(self, email):
        field = self.is_present(*lil.EMAIL_FIELD_LI)
        assert field != False, 'Error of InputField'
        field.send_keys(email)

    def login_password_field(self, password):
        field = self.is_present(*lil.PASSWORD_FIELD_LI)
        assert field != False, 'Error of InputField'
        field.send_keys(password)

    def register_email_field(self, email):
        field = self.is_present(*lil.EMAIL_FIELD_REG)
        assert field != False, 'Error of InputField'
        field.send_keys(email)

    def register_password_field(self, password):
        field = self.is_present(*lil.PASSWORD_FIELD_REG)
        assert field != False, 'Error of InputField'
        field.send_keys(password)

    def register_password_field2(self, password):
        field = self.is_present(*lil.PASSWORD_FIELD_REG2)
        assert field != False, 'Error of InputField'
        field.send_keys(password)

    def login_buttton(self):
        button = self.is_present(*lil.BUTTON_LOGIN)
        assert button != False, 'Error of Button'
        button.click()

    def register_buttton(self):
        button = self.is_present(*lil.BUTTON_REGISTER)
        assert button != False, 'Error of Button'
        button.click()

    def forgot_password_buttton(self):
        button = self.is_present(*lil.BUTTON_FORGOT_PASSWORD)
        assert button != False, 'Error of Button'
        button.click()