from pages.sb_main_page import SBMainPage


class TestMainPage:

    @staticmethod
    def test_go_to_bun(driver):
        main_page = SBMainPage(driver)
        main_page.go_to_web()
        main_page.click_on_sauses_button()
        main_page.click_on_bun_button()

        header = main_page.check_section_bun()

        assert header.text == 'Булки'

    @staticmethod
    def test_go_to_sauses(driver):
        main_page = SBMainPage(driver)
        main_page.go_to_web()
        main_page.click_on_sauses_button()

        header = main_page.check_section_sauses()

        assert header.text == 'Соусы'

    @staticmethod
    def test_go_to_topping(driver):
        main_page = SBMainPage(driver)
        main_page.go_to_web()
        main_page.click_on_topping_button()

        header = main_page.check_section_topping()

        assert header.text == 'Начинки'
