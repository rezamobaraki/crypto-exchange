POETRY=poetry
MANAGE=src/manage.py
ENV_FILE=config.env

# Load environment variables from config.env
ifneq (,$(wildcard $(ENV_FILE)))
    include $(ENV_FILE)
    export $(shell sed 's/=.*//' $(ENV_FILE))
endif

.PHONY: help install runserver runserver-plus migrate make-migration dump-data create-superuser db-shell shell shell-plus show-urls test lint collect-static make-messages compile-messages build prepare-compose up up-force-build down

help: ## Show this help
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ""

install: ## Install dependencies
	$(POETRY) install

runserver: ## Run the Django development server
	$(POETRY) run $(MANAGE) runserver

runserver-plus: ## Run the Django development server_plus
	$(POETRY) run $(MANAGE) runserver_plus

migrate: ## Apply database migrations
	$(POETRY) run $(MANAGE) migrate

make-migration: ## Create a migration
	$(POETRY) run $(MANAGE) makemigrations

dump-data: ## Dump data
	$(POETRY) run $(MANAGE) dumpdata

create-superuser: ## Create a superuser
	$(POETRY) run $(MANAGE) createsuperuser

db-shell: ## Run the Django database-shell
	$(POETRY) run $(MANAGE) dbshell

shell: ## Run the Django shell
	$(POETRY) run $(MANAGE) shell

shell-plus: ## Run the Django shell plus with print-sql
	$(POETRY) run $(MANAGE) shell_plus --print-sql

show-urls: ## Show all urls
	$(POETRY) run $(MANAGE) show_urls

test: ## Run tests
	$(POETRY) run $(MANAGE) test

lint: ## Run linters
	$(POETRY) run flake8 src/

collect-static: ## Collect static files
	$(POETRY) run $(MANAGE) collectstatic

make-messages: ## Create messages
	cd ./src && $(POETRY) run $(MANAGE) makemessages -l fa

compile-messages: ## Compile messages
	cd ./src && $(POETRY) run $(MANAGE) compilemessages

build: ## Build the Docker image
	sudo docker build . -t goodreads:latest -f Dockerfile

prepare-compose: ## Prepare the docker-compose environment
	@[ -d .compose ] || mkdir .compose

	@if [ ! -f .compose/config.env ]; then \
		cp config.example .compose/config.env; \
		sed -i -e 's/localhost:6379/redis:6379/g' .compose/config.env; \
		sed -i -e 's/POSTGRES_NAME=NAME/POSTGRES_NAME=boilerplate/g' .compose/config.env; \
		sed -i -e 's/POSTGRES_USER=USER/POSTGRES_USER=postgres/g' .compose/config.env; \
		sed -i -e 's/POSTGRES_PASSWORD=PASSWORD/POSTGRES_PASSWORD=postgres/g' .compose/config.env; \
		sed -i -e 's/POSTGRES_HOST=HOST/POSTGRES_HOST=postgres/g' .compose/config.env; \
		sed -i -e 's/REDIS_HOST=LOCALHOST/REDIS_HOST=redis/g' .compose/config.env; \
	fi;

up: prepare-compose ## Start the Docker containers
	sudo docker-compose up -d

up-force-build: prepare-compose ## Start the Docker containers and force a rebuild
	sudo docker-compose up -d --build

down: ## Stop the Docker containers
	sudo docker-compose down