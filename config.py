# config.py
import os


class Settings:
    """
    Configurações básicas da aplicação, lidas de variáveis de ambiente.

    Em um projeto maior, isso poderia usar Pydantic Settings, dotenv etc.
    Aqui vamos usar os.getenv para simplificar o lab.
    """

    APP_NAME: str = os.getenv("APP_NAME", "CareOps+")
    APP_ENV: str = os.getenv("APP_ENV", "dev")  # dev, stg, prod etc.

    # NUNCA usar esses defaults em produção.
    # Eles existem apenas para facilitar desenvolvimento/local.
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-insecure-secret-key")

    # Exemplo de URL de banco de dados (para dev usamos sqlite local)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./dev.db")


settings = Settings()