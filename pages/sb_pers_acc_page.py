from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LocatorPersAccPage:
    LOCATOR_HEAD_PERS_ACC_PAGE = (By.XPATH, "//a[@href='/account/profile']")  # Заголовок страницы
    LOCATOR_LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")  # Кнопка Выход


class SBPersAccPage(BasePage):

    def check_head_pers_acc_page(self):
        return self.find_element(LocatorPersAccPage.LOCATOR_HEAD_PERS_ACC_PAGE)

    def click_on_logout_button(self):
        return self.click_on_button(LocatorPersAccPage.LOCATOR_LOGOUT_BUTTON)
