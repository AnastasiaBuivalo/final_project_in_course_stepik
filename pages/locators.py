from selenium.webdriver.common.by import By

#каждый класс локатор соответствует одной странице
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
     LOGIN_FORM = (By.ID, "login_form")
     REGISTER_FORM = (By.ID, "register_form")
     REGISTER_EMAIL = (By.ID, "id_registration-email")
     REGISTER_PASSWORD1 = (By.ID, "id_registration-password1")
     REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")
     REGISTER_BTN = (By.CSS_SELECTOR, "#id_registration-redirect_url+button")

class ProductPageLocators():
    BTN_ADD_PRODUCT = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_BASKET = (By.CSS_SELECTOR,".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ITEMS_PRODUCTS = (By.CSS_SELECTOR, ".basket-items .row")
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    