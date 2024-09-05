import allure
from selenium.webdriver.common.by import By

from config.config import Config
from ui_tests.locators.locators import MainPageLocators
from ui_tests.page.base_page import BasePage

config = Config.load_from_json()


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.card_title = None
        self.card_old_price = None
        self.card_discount_price = None

    @allure.step("Нажать на кнопку 'Найти'")
    def click_on_find_button(self):
        self.click_element((By.CSS_SELECTOR, MainPageLocators.SEARCH_BUTTON))

    @allure.step("Заполнить поле поиска")
    def fill_search_field(self, text):
        self.send_keys_to_element(
            (By.CSS_SELECTOR, MainPageLocators.SEARCH_INPUT), text)

    @allure.step("Проверить, что поле заполнено ожидаемым значением")
    def assert_search_field_value(self, expected_value):
        self.assert_field_value(
            (By.CSS_SELECTOR, MainPageLocators.SEARCH_INPUT), expected_value)

    @allure.step("Проверить поисковую выдачу")
    def assert_search_results(self, expected_value):
        self.assert_element_contains_text(
            (By.CSS_SELECTOR, MainPageLocators.PRODUCT_TITLE_HEAD), expected_value)

    @allure.step("Нажать на кнопку 'Купить' у карточки товара")
    def click_on_product_buy_button(self):
        self.click_element(
            (By.CSS_SELECTOR, MainPageLocators.PRODUCT_BUY_BUTTON))

    @allure.step("Сохранить название карточки товара")
    def save_product_card_name(self):
        self.card_title = self.get_text_element(
            (By.CSS_SELECTOR, MainPageLocators.PRODUCT_TITLE_HEAD))

    @allure.step("Сохранить старую цену карточки товара")
    def save_product_card_old_price(self):
        self.card_old_price = self.get_text_element(
            (By.CSS_SELECTOR, MainPageLocators.PRODUCT_OLD_PRICE))

    @allure.step("Сохранить скидочную цену карточки товара")
    def save_product_card_discount_price(self):
        self.card_discount_price = self.get_text_element(
            (By.CSS_SELECTOR, MainPageLocators.PRODUCT_DISCOUNT_PRICE))

    @allure.step("Нажать на кнопк 'Оформить'")
    def click_checkout_button(self):
        self.click_element(
            (By.XPATH, MainPageLocators.PRODUCT_CHECKOUT_BUTTON))

    @allure.step("Проскролить динамическую страницу вниз")
    def scroll_down_dynamic_page(self):
        self.scroll_down()

    @allure.step("Нажать на корзину в хедере")
    def click_header_cart_button(self):
        self.click_element(
            (By.CSS_SELECTOR, MainPageLocators.HEADER_CART_BUTTON))

    @allure.step("Подождать пока отобразиться бейджик у корзины")
    def wait_cart_badge_is_displayed(self):
        self.wait_element_is_displayed(
            (By.CSS_SELECTOR, MainPageLocators.HEADER_CART_BUBBLE))
