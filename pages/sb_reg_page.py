from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LocatorRegPage:
    LOCATOR_NAME_INPUT = (By.XPATH, '//fieldset[1]//input')  # Поле ввода имени
    LOCATOR_EMAIL_INPUT = (By.XPATH, '//fieldset[2]//input')  # Поле ввода почты
    LOCATOR_PASSWORD_INPUT = (By.XPATH, '//fieldset[3]//input')  # Поле ввода пароля
    LOCATOR_REG_BUTTON = (By.XPATH, "//form/button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    LOCATOR_HEAD_REG_FORM = (By.XPATH, "//main//h2[text()='Регистрация']")  # Заголовок страницы
    LOCATOR_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")  # Кнопка "Войти"


class SBRegPage(BasePage):

    def enter_name(self, text):
        return self.enter_text(LocatorRegPage.LOCATOR_NAME_INPUT, text)

    def enter_email(self, text):
        return self.enter_text(LocatorRegPage.LOCATOR_EMAIL_INPUT, text)

    def enter_password(self, text):
        return self.enter_text(LocatorRegPage.LOCATOR_PASSWORD_INPUT, text)

    def click_on_reg_button(self):
        return self.click_on_button(LocatorRegPage.LOCATOR_REG_BUTTON)

    def check_head_reg_page(self):
        return self.find_element(LocatorRegPage.LOCATOR_HEAD_REG_FORM)

    def click_on_login_link(self):
        return self.click_on_button(LocatorRegPage.LOCATOR_LOGIN_LINK)

    def registration(self, name, email, password):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_on_reg_button()
