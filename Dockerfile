# Use a imagem base oficial do Python 3.12
FROM python:3.12-slim

# Configurações do Python para melhor performance e logs em ambientes docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copia o binário oficial do `uv` recém compilado, garantindo alta velocidade de instalação
# Como a sua versão no requirements estava travada na 0.11.2, usaremos a correspondente ou mais recente.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Define a pasta onde nossa aplicação ficará dentro do container
WORKDIR /

# Copia os arquivos de configuração de pacotes primeiro (garantindo otimização de Cache do Docker)
COPY pyproject.toml uv.lock ./

# Instala todas as dependências de produção do projeto
# O --frozen garante que usaremos estritamente as versões do seu uv.lock
RUN uv sync --frozen --no-dev --no-install-project

# Copia especificamente apenas o que é estritamente necessário para rodar o app
COPY src ./src
COPY entrypoint.py ./

# Finaliza a sincronização instalando o projeto atual
RUN uv sync --frozen --no-dev

# Define o que o container vai rodar quando ele iniciar
CMD ["uv", "run", "python", "entrypoint.py"]
