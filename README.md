# API - Projeto de Modernização do Manejo

[![CI](https://github.com/henriquesebastiao/modernizacao-manejo-api/actions/workflows/test.yml/badge.svg)](https://github.com/henriquesebastiao/modernizacao-manejo-api/actions/workflows/test.yml)
[![coverage](https://coverage-badge.samuelcolvin.workers.dev/henriquesebastiao/modernizacao-manejo-api.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/henriquesebastiao/modernizacao-manejo-api)
[![fastapi](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![postgresql](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)

API para o backend do projeto de modernização do manejo desenvolvida com FastAPI.

Esta API, construída com FastAPI, é a parte central de um projeto voltado para o setor agropecuário. Nosso objetivo é viabilizar uma gestão eficiente de informações sobre o rebanho de bovinos e seu desempenho, auxiliando os produtores rurais a tomar decisões mais assertivas e estratégicas.

A API visa proporcionar uma solução abrangente para o controle eficiente de informações relacionadas ao gado. Através dela, oferecemos funcionalidades robustas para realizar operações de CRUD no banco de dados, abrangendo desde o registro inicial até as análises avançadas de desempenho.

### Deploy 🚀

Você pode acessar a API [aqui](https://manejo-api.henriquesebastiao.com/).

Você também pode visualizar o deploy do banco de dados usando Adminer neste [link](https://adminer.henriquesebastiao.com/?pgsql=projects_postgres&username=manejo&db=manejo&ns=public).

Use a senha `manejo123`.

> Este usuário é apenas para leitura, fique a vontade para bisbilhotar :)

### Tecnologias utilizadas

- **Python** e **FastAPI**, para o desenvolvimento de uma API asyncrona e robusta.
- **Postgres** como banco de dados.
- **SQLAlchemy**, para interação com o banco de dados via ORM.
- **Pydantic**, para validação de dados.
- **PyTest**, para testes de integração.
- **Docker**, para desenvolvimento em containers.
- **Ruff** como linter e formatador de código.

## Principais Recursos

CRUD Completo: Gerencie suas informações sobre o gado com facilidade, desde a adição de novos registros até a atualização e exclusão de dados existentes.

Análises de Desempenho: Utilize recursos avançados para avaliar o desempenho do gado, possibilitando a tomada de decisões mais estratégicas no manejo.

## Executar Localmente

Toda a aplicação pode ser executada via Docker, logo você precisa somente dele instalado! ✅

Clone o repositório e entre nele com o seguinte comando:

```bash
git clone https://github.com/henriquesebastiao/modernizacao-manejo-api && cd modernizacao-manejo-api
```

Crie um arquivo `.env` que conterá as variáveis de ambiente exigidas pela aplicação, você pode fazer isso apenas copiando o arquivo de exemplo:

```bash
cat .env.example > .env
```

Agora execute o docker compose e toda aplicação será construída e iniciada 🚀

```bash
docker compose up -d
```

Pronto! Você já pode abrir seu navegador e acessar as seguintes URLs:

- Documentação interativa automática com Swagger UI (do backend OpenAPI): [http://localhost:8000](http://localhost:8000)
- Adminer, para visualizar facilmente o banco de dados: [http://localhost:8080](http://localhost:8080)
- Redoc, uma versão mais legível da documentação: [http://localhost:8000/redoc](http://localhost:8000/redoc)

Para acessar o banco de dados local pelo Adminer, selecione o sistema PostgreSQL e use as seguintes credenciais:

- Servidor: `database`
- Usuário: `user`
- Senha: `password`
- Banco de dados: `db`
