import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helpers.api_client import ApiClient


@pytest.fixture(scope="function")
def setup(request):
    chrome_options = Options()
    # Максимизируем окно браузера
    chrome_options.add_argument("--start-maximized")
    # Скрываем, что это автоматизированный браузер
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled")
    chrome_options.page_load_strategy = 'eager'  # 'normal', 'eager', 'none'
    # Игнорировать ошибки SSL
    chrome_options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(options=chrome_options)
    # request.cls.driver = driver, создает атрибут driver в тестовом классе, который будет доступен для всех методов этого класса.
    request.cls.driver = driver
    open_url(driver)

    yield driver
    driver.quit()


@allure.step("Открыть главную страницу Читай-Город")
def open_url(driver):
    driver.get("https://www.chitai-gorod.ru/")


@pytest.fixture
def api_client():
    return ApiClient()
