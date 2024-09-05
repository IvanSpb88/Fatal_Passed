# Проект автоматизации UI- и API-тестов.

### Настройка проекта

1. Создайте виртуальное окружение:  
   `python -m venv .venv`

2. Активируйте виртуальное окружение:
    - На Windows:  
      `.venv\Scripts\activate`
    - На macOS и Linux:  
      `source .venv/bin/activate`
3. Установите необходимые зависимости:  
   `pip install -r requirements.txt`

### Запуск тестов

Предусловия: Указать токен в config.json

1. <u>Обычный запуск тестов с помощью pytest:</u>  
   `pytest .\api_tests\tests\api_tests.py`  
   `pytest .\ui_tests\tests\ui_tests.py`

2. <u>Для генерации и просмотра отчета Allure в браузере</u>
    - Установить Allure через npm:  
      `npm install -g allure-commandline`
    - Далее выполнить:
        - `pytest .\api_tests\tests\api_tests.py --alluredir allure-results`
        - `pytest .\api_tests\tests\ui_tests.py --alluredir allure-results`
        - `allure serve ./allure-results`
    - После выполнения allure serve автоматически откроется браузер с отчетом. Если отчет пустой, значит в папке
      allure-results ничего не сгенерировалось.

---

#### Для запуска тестов несколько раз с помощью pytest-repeat, вы можете использовать параметр _**--count**_:

`pytest --count=10 your_test_file.py`

    `--count=10` — параметр, указывающий количество повторений тестов.  
    `your_test_file.py` — имя файла с тестами, которые вы хотите запустить.

---
<br>Ссылка на репозиторий: https://github.com/IvanSpb88/skypro_Diplom.git