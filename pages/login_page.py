from .base_page import BasePage
from .locators import LogInLocators as lil

class LogInPage (BasePage):
    def login_email_field(self, email):
        """
        _summary_

        Inputs the given email into the email field to log in.

        Args:
            email (str): The email to be entered into the login email field.

        Example:
            page.login_email_field("user@example.com")
        """
        field = self.is_present(*lil.EMAIL_FIELD_LI)
        assert field != False, 'Error of InputField'
        field.send_keys(email)

    def login_password_field(self, password):
        """
        _summary_

        Inputs the given password into the password field to log in.

        Args:
            password (str): The password to be entered into the login password field.

        Example:
            page.login_password_field("password123")
        """
        field = self.is_present(*lil.PASSWORD_FIELD_LI)
        assert field != False, 'Error of InputField'
        field.send_keys(password)

    def register_email_field(self, email):
        """
        _summary_

        Inputs the given email into the email field to register.

        Args:
            email (str): The email to be entered into the registration email field.

        Example:
            page.register_email_field("user@example.com")
        """
        field = self.is_present(*lil.EMAIL_FIELD_REG)
        assert field != False, 'Error of InputField'
        field.send_keys(email)

    def register_password_field(self, password):
        """
        _summary_

        Inputs the given password into the password field to register.

        Args:
            password (str): The password to be entered into the registration password field.

        Example:
            page.register_password_field("password123")
        """
        field = self.is_present(*lil.PASSWORD_FIELD_REG)
        assert field != False, 'Error of InputField'
        field.send_keys(password)

    def register_password_field2(self, password):
        """
        _summary_

        Inputs the given password into the second registration password field for confirmation (it must be the same as the first option)

        Args:
            password (str): The password to be entered into the password confirmation field.

        Example:
            page.register_password_field2("password123")
        """
        field = self.is_present(*lil.PASSWORD_FIELD_REG2)
        assert field != False, 'Error of InputField'
        field.send_keys(password)

    def login_buttton(self):
        """
        _summary_

        Clicks the 'Login' button to submit the login form.

        Args:
            None

        Example:
            page.login_buttton()
        """
        button = self.is_present(*lil.BUTTON_LOGIN)
        assert button != False, 'Error of Button'
        button.click()

    def register_buttton(self):
        """
        _summary_

        Clicks the 'Register' button to submit the registration form.

        Args:
            None

        Example:
            page.register_buttton()
        """
        button = self.is_present(*lil.BUTTON_REGISTER)
        assert button != False, 'Error of Button'
        button.click()

    def forgot_password_buttton(self):
        """
        _summary_

        Clicks the 'Forgot Password' button to navigate to the password recovery page.

        Args:
            None

        Example:
            page.forgot_password_buttton()
        """
        button = self.is_present(*lil.BUTTON_FORGOT_PASSWORD)
        assert button != False, 'Error of Button'
        button.click()