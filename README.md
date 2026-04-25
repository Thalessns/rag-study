# RAG Study

Projeto de estudo de Retrieval-Augmented Generation (RAG) construído com Python. A aplicação fornece uma API utilizando FastAPI e integra bibliotecas como LangChain, ChromaDB e Google GenAI (Gemini) para o processamento e a recuperação de informações e documentos integrados a modelos de linguagem.

## Pré-requisitos

- Docker Compose (opcional)
- Chave de acesso da API do Google Gemini

## Configuração

Antes de iniciar o projeto, certifique-se de configurar as suas variáveis de ambiente. Crie um arquivo com o nome `.env` na raiz do projeto (caso não exista) e adicione a sua chave de API:

```env
GEMINI_API_KEY=sua_chave_de_api_aqui
```

## Como executar (Docker Compose)

O projeto possui um ambiente conteinerizado pronto para uso. Para rodar a aplicação, abra o terminal na raiz do projeto e execute o comando:

```bash
docker compose up
```

Caso deseje iniciar os containers em segundo plano (modo detached), você pode utilizar a flag `-d`:

```bash
docker compose up -d
```

Após a inicialização do container, a aplicação e a API estarão disponíveis localmente através do endereço:
`http://localhost:8000`

## Como executar (Localmente com uv)

Se preferir rodar a aplicação nativamente sem contêineres, você pode utilizar o gerenciador de pacotes `uv`.

1. Instale as dependências do projeto (isso configurará o ambiente virtual automaticamente):

```bash
uv sync
```

2. Execute o servidor de aplicação:

```bash
uv run python entrypoint.py
```

Assim como via Docker, a API ficará disponível em: `http://localhost:8000`

## Estrutura do projeto

- `src/`: Diretório contendo os componentes principais da aplicação, configurações e regras de negócio da API.
- `entrypoint.py`: Arquivo de entrada utilizado para iniciar o servidor Uvicorn.
- `Dockerfile`: Arquivo contendo as instruções para a construção da imagem da aplicação utilizando Python.
- `docker-compose.yml`: Arquivo responsável pela orquestração do container, configuração de portas e mapeamento dos volumes.
- `pyproject.toml`: Arquivo responsável por declarar as dependências do projeto de forma otimizada utilizando o gerenciador de pacotes uv.


## Swagger

O swagger da aplicação está disponível no endpoint `/docs`.
Então, basta acessar `http://localhost:8000/docs` no seu navegador para interagir com a API.
