from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LocatorMainPage:
    LOCATOR_HEAD_MAIN_PAGE = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок страницы
    LOCATOR_SECTOR_BUN = (By.XPATH, "//h2[text()='Булки']")  # Раздел "Булки"
    LOCATOR_SECTOR_SAUSES = (By.XPATH, "//h2[text()='Соусы']")  # Раздел "Соусы"
    LOCATOR_SECTOR_TOPPING = (By.XPATH, "//h2[text()='Начинки']")  # Раздел "Начинки"
    LOCATOR_BUN_BUTTON = (By.XPATH, "//span[text()='Булки']")  # Кнопка "Булки"
    LOCATOR_SAUSES_BUTTON = (By.XPATH, "//span[text()='Соусы']")  # Кнопка "Соусы"
    LOCATOR_TOPPING_BUTTON = (By.XPATH, "//span[text()='Начинки']")  # Кнопка "Начинки"


class SBMainPage(BasePage):

    def check_head_main_page(self):
        return self.find_element(LocatorMainPage.LOCATOR_HEAD_MAIN_PAGE)

    def check_section_bun(self):
        return self.find_element(LocatorMainPage.LOCATOR_SECTOR_BUN)

    def check_section_sauses(self):
        return self.find_element(LocatorMainPage.LOCATOR_SECTOR_SAUSES)

    def check_section_topping(self):
        return self.find_element(LocatorMainPage.LOCATOR_SECTOR_TOPPING)

    def click_on_bun_button(self):
        return self.click_on_button(LocatorMainPage.LOCATOR_BUN_BUTTON)

    def click_on_sauses_button(self):
        return self.click_on_button(LocatorMainPage.LOCATOR_SAUSES_BUTTON)

    def click_on_topping_button(self):
        return self.click_on_button(LocatorMainPage.LOCATOR_TOPPING_BUTTON)
