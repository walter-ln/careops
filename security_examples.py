# aluno/labs/aula5/security_examples.py
import hashlib
import re
import os

# substituimos o from . import database
try:
    # quando o pacote raiz estiver disponível (por exemplo: import careops.database)
    from careops import database
except ImportError:
    # quando o módulo for executado/importado como módulo de topo (ex.: tests que fazem `from security_examples import ...`)
    import database

def hash_password_insecure(password: str) -> str:
    """
    Versão melhorada (ainda simplificada):
    - Usa SHA-256 com salt aleatório.
    - Retorna salt + hash como hexdigest concatenado.
    """
    salt = os.urandom(16)  # 16 bytes aleatórios
    digest = hashlib.sha256(salt + password.encode()).hexdigest()

    # retorna salt+hash em hexa: tamanho total > 64
    return salt.hex() + digest

def build_user_query(username: str) -> str:
    """
    Versão didática mais segura:
    - Rejeita entradas com padrões suspeitos (ex.: ' OR '1'='1).
    - Em um sistema real, usaríamos parâmetros/ORM, não string concatenada.
    """

    payload_suspeito = ["'", "\"", " or ", " and ", ";", "--"]

    lower = username.lower()
    if any(token in lower for token in payload_suspeito):
        raise ValueError("Entrada de username suspeita de SQL Injection.")

    # Aqui continuamos simples, apenas para o exemplo:
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query


def sanitize_comment(comment: str) -> str:
    """
    Remove tags <script> e </script> (case-insensitive).
    Atenção: isso NÃO é uma solução completa de XSS,
    é apenas um exemplo didático.
    """
    # Remove tudo entre <script ...> e </script>
    sanitized = re.sub(r"(?is)<script.*?>.*?</script>", "", comment)

    return sanitized
