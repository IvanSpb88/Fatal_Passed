import allure
import pytest
from allure import step

from datasets.expected_response_dataset import ExpectedResponseDataset


@pytest.mark.usefixtures("api_client")
class TestAPI:

    @staticmethod
    def assert_response_status_code(response, expected_status_code):
        with allure.step(f"Проверить статус код: ожидается {expected_status_code}"):
            assert response.status_code == expected_status_code

    @staticmethod
    def assert_response_body(response, expected_body):
        with allure.step("Проверить тело ответа"):
            assert response.json() == expected_body

    @allure.title('Добавление книги в корзину')
    @allure.tag('POST')
    def test_add_book_to_cart(self, api_client):
        data = {
            "id": 3040901,
            "adData": {
                "item_list_name": "index",
                "product_shelf": "Новинки литературы"
            }
        }
        with step("Отправить запрос"):
            response = api_client.post("cart/product", data=data)
        self.assert_response_status_code(response, 200)
        with step("Проверить, что тело ответа пустое"):
            assert not response.text

    @allure.title('Предзаказ книги')
    @allure.tag('GET')
    def test_preorder_book(self, api_client):
        params = {
            "cityId": 2,
            "productId": 3044076,
            "quantity": 1,
            "userType": "individual"
        }
        with step("Отправить запрос"):
            response = api_client.get(
                "orders/summary-pre-order", params=params)
        self.assert_response_status_code(response, 200)
        self.assert_response_body(
            response, ExpectedResponseDataset.PREORDER_BOOK_RESPONSE)

    @allure.title('Удаление книги из корзины')
    @allure.tag('DELETE')
    def test_delete_book_from_cart(self, api_client):
        data = {
            "id": 3040901,
            "adData": {
                "item_list_name": "index",
                "product_shelf": "Новинки литературы"
            }
        }
        with step("Отправить запрос на добавление книги в корзину"):
            api_client.post("cart/product", data=data)
        with step("Отправить запрос на получение списка товаров из корзины"):
            product_id = api_client.get("cart").json()["products"][0]["id"]
        with step("Отправить запрос на удаление книги из корзины"):
            response = api_client.delete(f"cart/product/{product_id}")
        self.assert_response_status_code(response, 204)

    @allure.title('Удаление книги из корзины по несуществующему id')
    @allure.tag('DELETE')
    def test_delete_non_exist_book_from_cart(self, api_client):
        with step("Отправить запрос на удаление книги из корзины"):
            response = api_client.delete(f"cart/product/123")
        self.assert_response_status_code(response, 404)
        with step("Проверить тело ответа"):
            assert response.json()[
                       "message"] == ExpectedResponseDataset.DELETE_NON_EXIST_BOOK_RESPONSE["message"]

    @allure.title('Получение ошибки когда не передано тело запроса при добавлении книги в корзину')
    @allure.tag('POST')
    def test_bad_request_when_add_book_to_cart(self, api_client):
        with step("Отправить запрос"):
            response = api_client.post("cart/product")
        self.assert_response_status_code(response, 400)
        with step("Проверить тело ответа"):
            assert response.json()[
                       "message"] == ExpectedResponseDataset.BAD_REQUEST_RESPONSE["message"]
