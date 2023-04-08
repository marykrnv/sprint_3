from pages.sb_login_page import SBLoginPage
from pages.sb_main_page import SBMainPage
from pages.sb_nav_bar import SBNavBar
from pages.sb_pers_acc_page import SBPersAccPage


class TestMainPage:

    @staticmethod
    def test_go_to_main_page_from_pers_acc_click_on_logo(driver):
        login_page = SBLoginPage(driver)
        login_page.go_to_web('/login')
        login_page.login()

        nav_bar = SBNavBar(driver)
        nav_bar.click_on_pers_acc_link()

        pers_page = SBPersAccPage(driver)
        pers_page.check_head_pers_acc_page()

        nav_bar.click_on_logo_link()

        main_page = SBMainPage(driver)
        header = main_page.check_head_main_page()

        assert header.text == 'Соберите бургер'

    @staticmethod
    def test_go_to_main_page_from_pers_acc_click_on_constructor_link(driver):
        login_page = SBLoginPage(driver)
        login_page.go_to_web('/login')
        login_page.login()

        nav_bar = SBNavBar(driver)
        nav_bar.click_on_pers_acc_link()

        pers_page = SBPersAccPage(driver)
        pers_page.check_head_pers_acc_page()

        nav_bar.click_on_constuctor_link()

        main_page = SBMainPage(driver)
        header = main_page.check_head_main_page()

        assert header.text == 'Соберите бургер'
