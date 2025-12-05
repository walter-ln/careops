# Dockerfile – versão para CI (imagem slim + usuário não-root)

FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# (Opcional) instalar dependências de sistema estritamente necessárias
# RUN apt-get update && apt-get install -y --no-install-recommends <pacotes> \
#     && rm -rf /var/lib/apt/lists/*

# Cria usuário não-root
RUN useradd -m appuser

# Copia apenas requirements primeiro (melhor uso de cache)
COPY requirements.txt .

# Instala dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Ajusta permissões para o usuário não-root
RUN chown -R appuser /app

# Troca para o usuário não-root
USER appuser

# Variáveis de ambiente padrão (podem ser sobrescritas em runtime)
ENV APP_ENV=dev
ENV PORT=8000

# Expondo a porta usada pelo uvicorn
EXPOSE 8000

# Comando padrão da aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]