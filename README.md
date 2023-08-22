Configurando ambiente:

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