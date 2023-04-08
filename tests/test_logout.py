from pages.sb_login_page import SBLoginPage
from pages.sb_nav_bar import SBNavBar
from pages.sb_pers_acc_page import SBPersAccPage


class TestLogout:

    @staticmethod
    def test_logout(driver):
        login_page = SBLoginPage(driver)
        login_page.go_to_web('/login')
        login_page.login()

        nav_bar = SBNavBar(driver)
        nav_bar.click_on_pers_acc_link()

        pers_page = SBPersAccPage(driver)
        pers_page.check_head_pers_acc_page()
        pers_page.click_on_logout_button()

        header = login_page.check_head_login_page()

        assert header.text == 'Вход'
