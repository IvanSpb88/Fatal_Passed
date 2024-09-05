import json
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Config:
    ui_base_url: str = None
    api_base_url: str = None
    explicit_wait: int = None
    headers: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def load_from_json(cls):
        # Загрузка данных из JSON файла
        with open('config.json') as f:
            data = json.load(f)
        return cls(**data)

    def get_authorization_header(self):
        return self.headers.get("Authorization")
