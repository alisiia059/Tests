from selenium.webdriver.common.by import By

class BasePageLocators:
    SEARCH_FIELD = By.NAME, 'q'
    BUTTON_SEARCH = By.XPATH, '//*[@id="default"]/header/div[2]/div/div[2]/form/input'
    BUTTON_BUSKET = By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a'
    BUTTON_LOGIN = By.ID, 'login_link'
    BUTTON_DO = By.XPATH, '//*[@id="language_selector"]/button'
    CHANGE_LANGUAGE  = By.NAME, 'language'

class MainPageLocators:
    BUTTONS_BOOKS = [(By.XPATH, f'//*[@id="promotions"]/section[2]/ul/li[{num}]/article/div[2]/form/button') for num in range(1,5)]
    MESSAGE_REGISTER = By.CLASS_NAME, 'alertinner'

class LogInLocators:
    EMAIL_FIELD_LI = By.NAME, 'login-username'
    PASSWORD_FIELD_LI = By.NAME, 'login-password'
    EMAIL_FIELD_REG = By.NAME, 'registration-email'
    PASSWORD_FIELD_REG = By.ID, 'id_registration-password1'
    PASSWORD_FIELD_REG2 = By.NAME, 'registration-password2'
    BUTTON_LOGIN = By.NAME, 'login_submit'
    BUTTON_REGISTER = By.NAME, 'registration_submit'
    BUTTON_FORGOT_PASSWORD= By.XPATH, '//*[@id="login_form"]/p/a'
    
class ProductPageLocators:
    PRODUCT_NAME = By.CSS_SELECTOR, '.product_main > h1'
    PRODUCT_PRICE = By.CSS_SELECTOR, '.product_main > p'
    BUTTON_WRITE_REVIEW = By.ID, 'write_review'
    BUTTON_ADD_BUSKET = By.CLASS_NAME, 'btn-add-to-basket'
    TITLE_FIELD = By.NAME, 'title'
    BODY_FIELD = By.NAME, 'body'
    NAME_FIELD = By.NAME, 'name'
    EMAIL_FIELD= By.NAME, 'email'
    BUTTON_SAVE_REVIEW = By.XPATH, '//*[@id="add_review_form"]/fieldset/button'
    AFTER_ADDING_NAME = By.CSS_SELECTOR, '.alertinner > strong'
    AFTER_ADDING_PRICE = By.CSS_SELECTOR, '.alertinner > p > strong'

class BusketPageLocators:
    BUTTON_CONTINUE_SHOPPING = By.XPATH, '//*[@id="content_inner"]/p/a'
    BUTTON_BOOK_LINK = By.CLASS_NAME, 'thumbnail'
    BUTTON_BOOK_QUANTITY = By.ID, 'id_form-0-quantity'
    BUTTON_UPDATE = By.CSS_SELECTOR, '.input-group-btn > button'
    BUTTON_PROCEED_CHECKOUT = By.CLASS_NAME, 'btn-primary'
    BUTTON_TITLE = By.ID, 'id_title'
    BUTTON_FIRST_NAME = By.ID, 'id_first_name'
    BUTTON_LAST_NAME = By.ID, 'id_last_name'
    BUTTON_LINE1 = By.ID, 'id_line1'
    BUTTON_LINE2 = By.ID, 'id_line2'
    BUTTON_LINE3 = By.ID, 'id_line3'
    BUTTON_CITY = By.ID, 'id_line4'
    BUTTON_STATE = By.ID, 'id_state'
    BUTTON_POSTCODE = By.ID, 'id_postcode'
    BUTTON_COUNTRY = By.ID, 'id_country'
    BUTTON_PHONE_NUMBER = By.ID, 'id_phone_number'
    BUTTON_INSTRUCTIONS = By.ID, 'id_notes'
    BUTTON_CONTINUE = By.CLASS_NAME, 'btn-lg'
    BUTTON_RETURN_BUSKET = By.XPATH, '//*[@id="new_shipping_address"]/div[13]/div/a'

# moya strochka print(MainPageLocators.BUTTONS_BOOKS) дададададдааддадададааддададададададад
# кста
# рЕАл slaaaay
