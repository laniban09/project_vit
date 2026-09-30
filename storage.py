import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("data.json")


def load_data():
    if not DATA_FILE.exists():
        return {"students": {}, "attendance": {}, "marks": {}}

    with DATA_FILE.open(encoding="utf-8") as file:
        data = json.load(file)

    for section in ("students", "attendance", "marks"):
        if section not in data:
            data[section] = {}
    return data


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
