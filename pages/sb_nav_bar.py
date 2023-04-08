from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LocatorNavBar:
    LOCATOR_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a[@href='/']")  # Лого страницы
    LOCATOR_PERS_ACC_BUTTON = (By.XPATH, "//a[@href='/account']")  # Кнопка "Личный кабинет"
    LOCATOR_CONSTRUCTOR = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX']")  # Кнопка "Конструктор"


class SBNavBar(BasePage):

    def click_on_logo_link(self):
        return self.click_on_button(LocatorNavBar.LOCATOR_LOGO)

    def click_on_pers_acc_link(self):
        return self.click_on_button(LocatorNavBar.LOCATOR_PERS_ACC_BUTTON)

    def click_on_constuctor_link(self):
        return self.click_on_button(LocatorNavBar.LOCATOR_CONSTRUCTOR)
