sttc:
	docker compose -f docker-compose.prod.yml run --rm web python3 manage.py collectstatic --noinput

mgrt:
	docker compose run --rm web python3 manage.py makemigrations
	docker compose run --rm web python3 manage.py migrate

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

clean:
	docker rm -f $(shell docker ps -aq)

test:
	docker run --rm $(shell docker build -q -f Dockerfile.test .) coverage run manage.py test

shell:
	docker compose run --rm web python3 manage.py shell
