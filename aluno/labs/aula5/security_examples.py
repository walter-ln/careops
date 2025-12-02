# aluno/labs/aula5/security_examples.py

import hashlib
import os


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
    Constrói uma query SQL de forma insegura,
    concatenando o parâmetro diretamente.
    """
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query


def sanitize_comment(comment: str) -> str:
    """
    Implementação ingênua: apenas retorna o comentário.
    Não protege contra XSS (inserção de <script>, etc.).
    """
    return comment