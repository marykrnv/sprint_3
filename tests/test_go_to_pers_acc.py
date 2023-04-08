from pages.sb_login_page import SBLoginPage
from pages.sb_nav_bar import SBNavBar
from pages.sb_pers_acc_page import SBPersAccPage


class TestPersAcc:

    @staticmethod
    def test_go_to_pers_acc(driver):
        login_page = SBLoginPage(driver)
        login_page.go_to_web('/login')
        login_page.login()

        nav_bar = SBNavBar(driver)
        nav_bar.click_on_pers_acc_link()

        pers_page = SBPersAccPage(driver)
        header = pers_page.check_head_pers_acc_page()

        assert header.text == 'Профиль'
