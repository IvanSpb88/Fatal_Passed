import allure
import pytest

from page.cart_page import CartPage
from page.main_page import MainPage


@pytest.mark.usefixtures("setup")
class TestUI:

    @allure.feature('ID: Kurs 2')
    @allure.title('Поле для поиска принимает ввод данных')
    def test_search_input(self):
        main_page = MainPage(self.driver)
        main_page.fill_search_field("Математика")
        main_page.assert_search_field_value("Математика")

    @allure.feature('ID: Kurs 3')
    @allure.title('Кнопка поиска “Найти” работает корректно')
    def test_search_button(self):
        main_page = MainPage(self.driver)
        main_page.fill_search_field(
            "Математика. 1 класс. Рабочая тетрадь. В 2-х частях. Часть 1")
        main_page.click_on_find_button()
        main_page.assert_search_results(
            "Математика. 1 класс. Рабочая тетрадь. В 2-х частях. Часть 1")

    @allure.feature('ID: Kurs 4')
    @allure.title('Кнопка “Купить” работает корректно')
    def test_buy_button(self):
        main_page = MainPage(self.driver)
        cart_page = CartPage(self.driver)
        main_page.fill_search_field("Математика")
        main_page.click_on_find_button()
        main_page.click_on_product_buy_button()
        main_page.click_checkout_button()
        cart_page.assert_cart_item(main_page.card_title)

    @allure.feature('ID: Kurs 5')
    @allure.title('Кнопка “Оформить” работает корректно')
    def test_checkout_button(self):
        main_page = MainPage(self.driver)
        cart_page = CartPage(self.driver)
        main_page.fill_search_field("Математика")
        main_page.click_on_find_button()
        main_page.click_on_product_buy_button()
        main_page.click_checkout_button()
        cart_page.assert_cart_page_is_displayed()

    @allure.feature('ID: Kurs 6')
    @allure.title('Кнопка “Корзина” работает корректно')
    def test_card_button(self):
        main_page = MainPage(self.driver)
        cart_page = CartPage(self.driver)
        main_page.fill_search_field("Математика")
        main_page.click_on_find_button()
        main_page.click_on_product_buy_button()
        main_page.wait_cart_badge_is_displayed()
        main_page.click_header_cart_button()
        cart_page.assert_cart_item_price(
            main_page.card_old_price, main_page.card_discount_price)
