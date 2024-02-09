from .base_page import BasePage

from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "the login substring not found from the URL"
        # реализуйте проверку на корректный url адрес
        # assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"
        # реализуйте проверку, что есть форма логина
        # assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Rigister form not found"
        # реализуйте проверку, что есть форма регистрации на странице
        # assert True
    
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password1_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password2_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        email_field.send_keys(email)
        password1_field.send_keys(password)
        password2_field.send_keys(password)

        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()
        