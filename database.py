import json
from pathlib import Path

# database.py
"""Minimal stub 'database' module to satisfy imports in aluno/labs/aula5/security_examples.py.

Expand this stub with the real API if/when tests or code require it.
"""

def connect(*args, **kwargs):
    """Return a fake connection or None for tests."""
    return None

def get_user(username):
    """Return None or a minimal user dict for tests that might call it."""
    return None

class DummyDB:
    def __init__(self):
        self._store = {}
    def get(self, k, default=None):
        return self._store.get(k, default)
    def set(self, k, v):
        self._store[k] = v

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
