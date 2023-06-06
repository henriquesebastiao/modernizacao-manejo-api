requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

db-up:
	docker-compose up -d postgres
