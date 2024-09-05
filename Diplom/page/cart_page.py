import allure
from selenium.webdriver.common.by import By

from locators.locators import CartPageLocators
from page.base_page import BasePage


class CartPage(BasePage):

    @allure.step("Проверить, что в корзине лежит товар")
    def assert_cart_item(self, expected_value):
        self.assert_element_contains_text(
            (By.CSS_SELECTOR, CartPageLocators.CART_ITEM), expected_value)

    @allure.step("Проверить, что осуществлен переход на страницу корзины")
    def assert_cart_page_is_displayed(self):
        self.assert_element_contains_text(
            (By.CSS_SELECTOR, CartPageLocators.CART_PAGE_TITLE), "КОРЗИНА")
        self.assert_url("/cart")

    @allure.step("Проверить цены на товар в корзине")
    def assert_cart_item_price(self, expected_old_price, expected_discount_price):
        self.assert_element_contains_text(
            (By.CSS_SELECTOR, CartPageLocators.CARD_PRODUCT_OLD_PRICE), expected_old_price)
        self.assert_element_contains_text(
            (By.CSS_SELECTOR, CartPageLocators.CARD_PRODUCT_DISCOUNT_PRICE), expected_discount_price)
