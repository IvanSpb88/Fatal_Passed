from dotenv import dotenv_values


class Config:
    config = dotenv_values()

    UI_BASE_URL = config['UI_BASE_URL']
    API_BASE_URL = config['API_BASE_URL']
    EXPLICIT_WAIT = config['EXPLICIT_WAIT']
    AUTHORIZATION_TOKEN = config['AUTHORIZATION_TOKEN']
    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Authorization": f"Bearer {AUTHORIZATION_TOKEN}"
    }