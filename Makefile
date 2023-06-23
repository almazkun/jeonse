FILES = .
k = --parallel

lint:
	pipenv run isort --force-single-line-imports --line-width 999 ${FILES}
	pipenv run autoflake --ignore-init-module-imports --in-place --remove-all-unused-imports ${FILES}
	pipenv run isort --use-parentheses --trailing-comma --multi-line 3 --force-grid-wrap 0 --line-width 140 ${FILES}
	pipenv run black ${FILES}

up:	
	docker compose up -d --build
	docker ps -a

cov:
	docker compose exec web pip install coverage
	docker compose exec web coverage run ./manage.py test 
	docker compose exec web coverage html
	docker compose exec web coverage report -m

down:
	docker compose down	-v

_prod:
	docker compose -f docker-compose.prod.yml up -d --build
	docker ps -a

collectstatic:
	docker compose exec web python manage.py collectstatic --no-input

makemigrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate

startdemo:
	docker compose exec web python manage.py create_demo_user
	docker compose exec web python manage.py create_demo_listings

build:
	docker compose build

logs:
	docker compose logs -f

test:
	docker compose run --rm --entrypoint="python" web manage.py test ${k}

prod: _prod migrate collectstatic

prod_restart: down prod

ps:
	docker ps -a

fresh_start: down up collectstatic makemigrations migrate startdemo 

registry_build:
	docker build -t ghcr.io/almazkun/jeonse:0.1.0 .

registry_push:
	docker push ghcr.io/almazkun/jeonse:0.1.0

registry_pull:
	docker pull ghcr.io/almazkun/jeonse:0.1.0