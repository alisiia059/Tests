from .pages.base_page import BasePage as bp
from .pages.main_page import MainPage as mp
from .pages.login_page import LogInPage as lip
from .pages.product_page import ProductPage as pp
from .pages.busket_page import BusketPage as bup
import pytest
import string
import random
import time

def test_random(driver):
    page = bp(driver, 'https://selenium1py.pythonanywhere.com/ru/')
    page.open()
    page.choose_language('it')
    page.input_text_search_field('python')

def test_click_2book(driver): 
    page = mp(driver, 'https://selenium1py.pythonanywhere.com/en-gb/')
    page.open()
    page.check_b4ttons()
    page.click_button(2)

@pytest.mark.productpage
def test_buy_book_write_review(driver):
    page = pp(driver, 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/')
    page.open()
    page.add_book_busket()
    page.write_review('sa','sad','asd','asd@sa')

def random_email():
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
def test_register_user(driver):
    page = mp(driver, 'https://selenium1py.pythonanywhere.com/en-gb/')
    page.open()
    page.click_login()
    page = lip(driver, page.get_current_url())
    page.register_email_field(random_email())
    password = random_password()
    page.register_password_field(password)
    page.register_password_field2(password)
    page.register_buttton()
    page = mp(driver, page.get_current_url())
    page.check_messsage()

@pytest.mark.productpaage
@pytest.mark.busketpage
def test_make_order(driver):
    page = pp(driver, 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/neuromancer_13/')
    page.open()
    page.add_book_busket()
    page.view_busket()
    page = bup(driver, page.get_current_url())
    page.proceed_checkout()
    time.sleep(10)
    page.shipping_address()




    

