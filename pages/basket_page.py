from selenium.webdriver.common.by import By
from .locators import  BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_not_be_products(self):
       assert self.is_not_element_present(*BasketPageLocators.ITEMS_PRODUCTS), "Products is presented, but should not be"
       
    def should_dissapear_of_products(self):
       assert self.is_disappeared(*BasketPageLocators.ITEMS_PRODUCTS),"Products is not disappeared"

    def should_of_message_basket_is_empty(self):
       assert not self.is_not_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY),"MESSAGE_BASKET_IS_EMPTY is not disappeared"

