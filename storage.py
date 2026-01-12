import json
from typing import List, Dict

FILE_NAME = "users.json"


def load_users() -> List[Dict]:
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_users(users: List[Dict]) -> None:
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=2, ensure_ascii=False)