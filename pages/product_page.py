from .base_page import BasePage
import math
import time


from .locators import ProductPageLocators

class ProductPage(BasePage):
    product_name = ''
    product_price = ''
    product_decription = ''

    def should_be_price(self):
      assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), "Price of product not found"
      self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_name_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_description(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION), "Description of product not found"
        self.product_decription = self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION).text

    def should_be_add_button(self):
        assert self.browser.find_element(*ProductPageLocators.BTN_ADD_PRODUCT), "Add button of product not found"
        return self.browser.find_element(*ProductPageLocators.BTN_ADD_PRODUCT)
    
    def should_be_success(self):
       assert self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES), "Message of Success added product in cartnot found"
       return self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
    
    def check_success_message(self):
      msg_lst = self.should_be_success()
      assert len(msg_lst) == 3, "Success message not found"

      assert self.product_name == msg_lst[0].text, "Wrong name product added to basket"
      assert self.product_price == msg_lst[2].text, "Wrong price product added to basket"
    
    def add_product_to_cart(self):
        self.should_be_price()
        self.should_be_description()
        self.should_be_name_product()
        self.should_be_add_button().click()

        self.solve_quiz_and_get_code()

        self.check_success_message()

    def should_not_be_success_message(self):
       assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Success message is presented, but should not be"
    

    def should_dissapear_of_success_message(self):
       assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES),"Success message is not disappeared"
    
