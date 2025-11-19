import json
from pathlib import Path

DB_FILE = Path(__file__).parent / "patients.json"


def load_db():
    """Carrega o banco. Vulnerável: não valida estrutura."""
    if not DB_FILE.exists():
        default_data = {
            "patients": {
                "1": {"id": 1, "name": "Maria Silva", "age": 42, "diagnosis": "Hipertensão"},
                "2": {"id": 2, "name": "João Souza", "age": 55, "diagnosis": "Diabetes tipo 2"}
            }
        }
        save_db(default_data)
        return default_data

    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_db(data):
    """Salva arquivo inseguro, sem criptografia ou controle."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
