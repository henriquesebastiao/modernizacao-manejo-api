## API - Projeto de Modernização do Manejo

[![Deploy to Amazon ECS](https://github.com/henriquesebastiao/modernizacao-manejo-api/actions/workflows/aws.yml/badge.svg)](https://github.com/henriquesebastiao/modernizacao-manejo-api/actions/workflows/aws.yml)
[![Ruff](https://github.com/henriquesebastiao/modernizacao-manejo-api/actions/workflows/ruff.yml/badge.svg)](https://github.com/henriquesebastiao/modernizacao-manejo-api/actions/workflows/ruff.yml)

API para o backend do prejeto de modernização do manejo desenvolvida com FastAPI.

<hr>

### Configurando ambiente:

Ligar o banco de dados:
```bash
make up-db
```

Desligar o banco de dados:
```bash
make down-db
```

Criar migração:
```bash
make create-migration
```

Rodar migração:
```bash
make apply-migration
```

Reverter migração:
```bash
make revert-migration
```

### Utilizando as tasks:

Rodando o projeto:
```bash
task run
```

Analisando o código com linter:
```bash
task lint
```

Reformatando o código automaticamente:
```bash
task format
```

Rodando testes:
```bash
task test
```

Gerando relatório HTML de cobertura de testes:
```bash
task post_test
```
