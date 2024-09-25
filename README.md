### Django Boilerplate Project

This is a boilerplate project for Django, designed to help you get started quickly with a standard setup. It includes
configurations for Poetry, PostgreSQL, and various Django apps and middleware.

### Prerequisites

- Python 3.8+
- Poetry
- PostgreSQL

### Installation

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install dependencies:**
    ```sh
    poetry install
    ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory and add the following variables:
    ```env
    POSTGRES_NAME=<your-database-name>
    POSTGRES_USER=<your-database-user>
    POSTGRES_PASSWORD=<your-database-password>
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    ALLOWED_HOSTS=*
    CSRF_TRUSTED_ORIGINS=
    ```

4. **Apply database migrations:**
    ```sh
    poetry run python src/manage.py migrate
    ```

5. **Create a superuser:**
    ```sh
    poetry run python src/manage.py createsuperuser
    ```

### Usage

- **Run the development server:**
    ```sh
    poetry run python src/manage.py runserver
    ```

- **Run tests:**
    ```sh
    poetry run python src/manage.py test
    ```

- **Run linters:**
    ```sh
    poetry run flake8 src/
    ```

### Makefile Commands

This project includes a `Makefile` for common tasks:

- `make install`: Install dependencies
- `make runserver`: Run the Django development server
- `make migrate`: Apply database migrations
- `make make-migration`: Create a migration
- `make dump-data`: Dump data
- `make create-superuser`: Create a superuser
- `make db-shell`: Run the Django database shell
- `make shell`: Run the Django shell
- `make show-urls`: Show all URLs
- `make test`: Run tests
- `make lint`: Run linters
- `make collect-static`: Collect static files
- `make make-messages`: Create messages
- `make compile-messages`: Compile messages

### Docker Commands

This project includes Docker support with the following commands:

- `make build`: Build the Docker image
- `make build-local`: Build the Docker image using the local Dockerfile
- `make up`: Start the Docker containers
- `make up-force-build`: Start the Docker containers with a forced build
- `make down`: Stop the Docker containers

### Project Structure

```
├── Dockerfile
├── Makefile
├── README.md
├── config.example.env
├── docker-compose.yaml
├── poetry.lock
├── pyproject.toml
└── src
    ├── core
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── env.py
    │   ├── settings
    │   │   ├── __init__.py
    │   │   ├── django
    │   │   │   ├── __init__.py
    │   │   │   ├── base.py
    │   │   │   ├── local.py
    │   │   │   ├── production.py
    │   │   │   └── test.py
    │   │   └── third_parties
    │   │       ├── __init__.py
    │   │       ├── drf.py
    │   │       └── jwt.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
```

### License

This project is licensed under the MIT License..