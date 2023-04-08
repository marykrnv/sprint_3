import pytest

from pages.sb_login_page import SBLoginPage
from pages.sb_reg_page import SBRegPage


class TestRegistration:

    @staticmethod
    def test_reg_success(driver, email, password):
        reg_page = SBRegPage(driver)
        reg_page.go_to_web('/register')
        reg_page.registration('Ольга', email, password)

        login_page = SBLoginPage(driver)

        header = login_page.check_head_login_page()

        assert header.text == 'Вход'

    @staticmethod
    @pytest.mark.parametrize(
        argnames=['name', 'email', 'password'],
        argvalues=[('Ольга', '', '1234567'),
                   ('', 'yefervbbv@mail.ru', '1234567'),
                   ('Ольга', 'yefervbbv@mail.ru', ''),
                   ('Ольга', 'yefervbb', '345grfgf4vreg'),
                   ('Ольга', 'yefervbbv8732e243rb@mail.ru', '12345'),
                   ])
    def test_reg_fail(driver, name, email, password):
        reg_page = SBRegPage(driver)
        reg_page.go_to_web('/register')
        reg_page.registration(name, email, password)

        header = reg_page.check_head_reg_page()

        assert header.text == 'Регистрация'
