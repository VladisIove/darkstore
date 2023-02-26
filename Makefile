
RUN_IN_DEV_CONTAINER=docker-compose -f dev-docker-compose.yml exec portfolio_manager_dev

build:
	docker-compose -f dev-docker-compose.yml build --no-cache

up:
	docker-compose -f dev-docker-compose.yml up 

down:
	docker-compose -f dev-docker-compose.yml down

migrate:
	$(RUN_IN_DEV_CONTAINER) aerich upgrade