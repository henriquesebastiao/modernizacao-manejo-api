# Description: Makefile for project

.PHONY: export-requirements
export-requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

.PHONY: up-db
up-db:
	docker-compose up -d postgres

.PHONY: down-db
down-db:
	docker-compose down

.PHONY: revert-migration
revert-migration:
	@read -p "Por favor, forneça o número de migrações ou enter para base: " N; \
	N=$${N:-"base"}; \
	poetry run alembic downgrade $$N

.PHONY: create-migration
create-migration:
	@read -p "Por favor, forneça o nome da migração: " Nome; \
	if [ -z "$$Nome" ]; then \
		Nome="migrate"; \
	fi; \
	poetry run alembic revision --autogenerate -m $$Nome

.PHONY: apply-migration
apply-migration:
	poetry run alembic upgrade head