sttc:
	docker compose  -f docker-compose.prod.yml run web python3 manage.py collectstatic --noinput
run:
	docker compose up --build
dev:  
	docker compose up
prod: sttc
	docker compose -f docker-compose.prod.yml up -d
down:
	docker compose down -v
lint:
	pipenv run isort --recursive --force-single-line-imports --line-width 999 .
	pipenv run autoflake --recursive --ignore-init-module-imports --in-place --remove-all-unused-imports .
	pipenv run isort --recursive --use-parentheses --trailing-comma --multi-line 3 --force-grid-wrap 0 --line-width 88 .
	pipenv run black .
