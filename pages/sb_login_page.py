from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LocatorLoginPage:
    LOCATOR_LOGIN_ACC_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    LOCATOR_EMAIL_INPUT = (By.XPATH, '//fieldset[1]//input')  # Поле ввода почты
    LOCATOR_PASSWORD_INPUT = (By.XPATH, '//fieldset[2]//input')  # Поле ввода пароля
    LOCATOR_LOGIN_BUTTON = (By.XPATH, "//form/button[text()='Войти']")  # Кнопка "Войти"
    LOCATOR_HEAD_LOGIN_FORM = (By.XPATH, "//main//h2[text()='Вход']")  # Заголовок страницы


class SBLoginPage(BasePage):
    EMAIL = 'markir@mail.ru'
    PASSWORD = '123456'

    def enter_email(self, text):
        return self.enter_text(LocatorLoginPage.LOCATOR_EMAIL_INPUT, text)

    def enter_password(self, text):
        return self.enter_text(LocatorLoginPage.LOCATOR_PASSWORD_INPUT, text)

    def click_on_login_button(self):
        return self.click_on_button(LocatorLoginPage.LOCATOR_LOGIN_BUTTON)

    def click_on_login_acc_button(self):
        return self.click_on_button(LocatorLoginPage.LOCATOR_LOGIN_ACC_BUTTON)

    def check_head_login_page(self):
        return self.find_element(LocatorLoginPage.LOCATOR_HEAD_LOGIN_FORM)

    def login(self):
        self.enter_email(SBLoginPage.EMAIL)
        self.enter_password(SBLoginPage.PASSWORD)
        self.click_on_login_button()
