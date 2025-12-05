# aluno/labs/aula5/test_security_examples.py

import re
import hashlib

from aluno.labs.aula5.security_examples import (
    hash_password_insecure,
    build_user_query,
    sanitize_comment,
)


def test_hash_password_deve_ser_resistente():
    """
    Exemplo de "requisito de segurança" expresso em teste:

    - Não queremos algoritmos de hash fracos (como MD5).
    - Queremos um hash com tamanho >= 64 caracteres, típico de SHA-256.
    """
    password = "SuperSenha!123"

    digest = hash_password_insecure(password)

    # Este teste FOI FEITO PARA FALHAR no código inicial.
    # O MD5 gera hexdigest de 32 caracteres, então isto deve acusar falha.
    assert len(digest) >= 64, "Hash muito curto: suspeita de algoritmo fraco (ex. MD5)"


def test_build_user_query_nao_deve_permitir_sql_injection():
    """
    Queremos que entradas maliciosas NÃO gerem queries inseguras.

    Cenário:
    - Um atacante envia username = \"admin' OR '1'='1\"
    - A query concatenada ficaria vulnerável.

    Nosso requisito:
    - A função deve proteger contra esse tipo de input
      (nesse exemplo didático, esperamos que levante uma exceção).
    """
    payload_malicioso = "admin' OR '1'='1"

    try:
        query = build_user_query(payload_malicioso)
    except ValueError:
        # Implementação segura pode optar por levantar ValueError → ok.
        return

    # Se não levantou erro, verificamos se a query ficou obviamente vulnerável:
    assert "OR '1'='1'" not in query, "Query vulnerável a SQL Injection detectada."


def test_sanitize_comment_remove_tags_script():
    """
    Queremos que comentários exibidos em HTML não permitam execução de <script>.

    Requisito:
    - Qualquer <script> deve ser removido do texto exibido.
    - É uma simplificação didática. Em produção, usar bibliotecas especializadas.
    """
    comment = "<b>Olá</b> <script>alert('xss');</script> mundo!"

    sanitized = sanitize_comment(comment)

    # Não queremos nenhuma tag <script> no resultado:
    assert "<script" not in sanitized.lower()
    assert "</script" not in sanitized.lower()

    # Opcionalmente, queremos manter parte do texto legível:
    assert "Olá" in sanitized
    assert "mundo" in sanitized
