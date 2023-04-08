from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LocatorForgotPassPage:
    LOCATOR_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")  # Кнопка "Войти"


class SBForgotPassPage(BasePage):

    def click_on_login_link(self):
        return self.click_on_button(LocatorForgotPassPage.LOCATOR_LOGIN_LINK)
