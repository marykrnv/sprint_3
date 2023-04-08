from pages.sb_forgot_pd_page import SBForgotPassPage
from pages.sb_login_page import SBLoginPage
from pages.sb_main_page import SBMainPage
from pages.sb_nav_bar import SBNavBar
from pages.sb_reg_page import SBRegPage


class TestLogin:

    @staticmethod
    def test_login_by_button_log_in_acc(driver):
        login_page = SBLoginPage(driver)
        login_page.go_to_web()
        login_page.click_on_login_acc_button()
        login_page.login()

        main_page = SBMainPage(driver)
        header = main_page.check_head_main_page()

        assert header.text == 'Соберите бургер'

    @staticmethod
    def test_login_by_pers_acc_link(driver):
        login_page = SBLoginPage(driver)
        login_page.go_to_web()

        nav_bar = SBNavBar(driver)
        nav_bar.click_on_pers_acc_link()
        login_page.login()

        main_page = SBMainPage(driver)
        header = main_page.check_head_main_page()

        assert header.text == 'Соберите бургер'

    @staticmethod
    def test_login_by_login_link_from_reg_page(driver):
        reg_page = SBRegPage(driver)
        reg_page.go_to_web('/register')
        reg_page.click_on_login_link()

        login_page = SBLoginPage(driver)
        login_page.login()

        main_page = SBMainPage(driver)
        header = main_page.check_head_main_page()

        assert header.text == 'Соберите бургер'

    @staticmethod
    def test_login_by_login_button_from_forgot_pass_page(driver):
        fp_page = SBForgotPassPage(driver)
        fp_page.go_to_web('/forgot-password')
        fp_page.click_on_login_link()

        login_page = SBLoginPage(driver)
        login_page.login()

        main_page = SBMainPage(driver)
        header = main_page.check_head_main_page()

        assert header.text == 'Соберите бургер'
