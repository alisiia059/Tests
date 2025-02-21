from .pages.base_page import BasePage as bp
from .pages.main_page import MainPage as mp
from .pages.login_page import LogInPage as lip
from .pages.product_page import ProductPage as pp
from .pages.busket_page import BusketPage as bup
import pytest
import string
import random
import time

@pytest.mark.basepage
def test_random(driver):
    """
    _summary_

    Test for the base page: Open the page, choose a language, and search for a term.

    Args:
        driver (WebDriver): The WebDriver instance used for the test.

    Example:
        test_random(driver)
    """
    page = bp(driver, 'https://selenium1py.pythonanywhere.com/ru/')
    page.open()
    page.choose_language('it')
    page.input_text_search_field('python')

@pytest.mark.mainpage
def test_click_2book(driver): 
    """
    _summary_

    Test for the main page: Check buttons and click the 2nd book button.

    Args:
        driver (WebDriver): The WebDriver instance used for the test.

    Example:
        test_click_2book(driver)
    """
    page = mp(driver, 'https://selenium1py.pythonanywhere.com/en-gb/')
    page.open()
    page.check_b4ttons()
    page.click_button(2)

@pytest.mark.productpage
def test_buy_book_write_review(driver):
    """
    _summary_

    Test for product page: Add book to the basket and write a review.

    Args:
        driver (WebDriver): The WebDriver instance used for the test.

    Example:
        test_buy_book_write_review(driver)
    """
    page = pp(driver, 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/')
    page.open()
    page.add_book_busket()
    page.write_review('title','body','name','user@example.com')

def random_email():
    """
    _summary_

    Generates a random email address for user registration.

    Args:
        None

    Returns:
        str: A randomly generated email address.

    Example:
        random_email()
    """
    email = ''
    for _ in range (10):
        ran = random.randint(1,3)
        if ran == 1:
            email += random.choice(string.ascii_lowercase)
        elif ran == 2:
            email += random.choice(string.ascii_uppercase)
        else:
            email += random.choice(string.digits)
    email += '@gmail.com'
    return (email)

def random_password():
    """
    _summary_

    Generates a random password for user registration.

    Args:
        None

    Returns:
        str: A randomly generated password.

    Example:
        random_password()
    """
    password = ''
    for _ in range (19):
        ran = random.randint(1,3)
        if ran == 1:
            password += random.choice(string.ascii_lowercase)
        elif ran == 2:
            password += random.choice(string.ascii_uppercase)
        else:
            password += random.choice(string.digits)
    return (password)

@pytest.mark.mainpage
@pytest.mark.loginpage
def test_register_user(driver):
    """
    _summary_

    Test for user registration: Create a new user with a random email and password.

    Args:
        driver (WebDriver): The WebDriver instance used for the test.

    Example:
        test_register_user(driver)
    """
    page = mp(driver, 'https://selenium1py.pythonanywhere.com/en-gb/')
    page.open()
    page.click_login()
    page = lip(driver, page.get_current_url())

    page.register_email_field(random_email())

    password = random_password()
    page.register_password_field(password)
    page.register_password_field2(password)
    page.register_buttton()

    # Check if registration is successful by checking the message or URL
    page = mp(driver, page.get_current_url())
    page.check_messsage() # Assert message or page state after registration

@pytest.mark.productpaage
@pytest.mark.busketpage
def test_make_order(driver):
    """
    _summary_

    Test for making an order: Add a book to the basket and proceed to checkout.

    Args:
        driver (WebDriver): The WebDriver instance used for the test.

    Example:
        test_make_order(driver)
    """
    page = pp(driver, 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/neuromancer_13/')
    page.open()
    page.add_book_busket()
    page.view_busket()

    page = bup(driver, page.get_current_url())
    page.proceed_checkout()

    time.sleep(10)
    page.shipping_address()




    

