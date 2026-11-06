# How to run

There are two ways to run the project. **Choose one:**

1. **Via Docker Compose**: starts the API and PostgreSQL in containers. This is
   the simplest way to run the full project.
2. **Locally**: starts the API directly on your machine. In this case, you need
   a PostgreSQL instance running and configured separately.

The instructions for each option are below. In both cases, the API exposes the
same endpoints; only the address changes: `http://localhost:8080` via Docker
Compose or `http://localhost:5000` locally.

## Requirements

- Docker with Docker Compose; or Python 3.10+ and PostgreSQL to run without Docker.

## Environment variables

Create a `.env` file at the project root:

```env
DATABASE_HOST=database
DATABASE_NAME=backend
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
```

These variables are used by the application to connect to the database. In Docker
Compose, `DATABASE_HOST` must be `database`, the PostgreSQL service name. For
local API execution, set `DATABASE_HOST` to the address of the PostgreSQL
instance accessible from your machine (for example, `localhost`).

| Variable            | Description            |
| ------------------- | ---------------------- |
| `DATABASE_HOST`     | PostgreSQL server host |
| `DATABASE_NAME`     | Database name          |
| `DATABASE_USER`     | Database user          |
| `DATABASE_PASSWORD` | Database user password |

The `.env` file contains credentials and should not be shared or committed to
version control.

## Run with Docker Compose

At the project root, with the `.env` configured, run:

```bash
docker compose up --build
```

The API will be available at `http://localhost:8080`. PostgreSQL is started
alongside the API, and the `init.sql` file creates the `users` table and inserts
sample records on the first initialization of the database volume.

To stop the services, press `Ctrl+C` and run:

```bash
docker compose down
```

## Run locally

With PostgreSQL running and the environment variables configured for that
database:

Create and activate the Python virtual environment:

```bash
python -m venv .venv       # Creates a virtual environment in the .venv directory
source .venv/bin/activate  # Activates the virtual environment (Linux/macOS)
```

On Windows PowerShell, use this command to activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies and start the API:

```bash
pip install -r requirements.txt
python app.py
```

When running locally, the API listens on port `5000`. Configure the database with
the same structure defined in `init.sql` before querying `/users`.

## Endpoints

### `GET /health`

Checks the connection to PostgreSQL.

```bash
curl -i http://localhost:8080/health
```

When the connection works, the response is `200 OK`:

```json
{
	"message": "Database connection is working!"
}
```

If the connection fails, the route returns `503 Service Unavailable`.

### `GET /users`

Returns the users registered in the `users` table.

```bash
curl -i http://localhost:8080/users
```

With records available, the response is `200 OK`, for example:

```json
{
	"message": "Users retrieved successfully!",
	"users": [
		{
			"id": 1,
			"name": "JOSÉ",
			"email": "jose@gmail.com"
		}
	]
}
```

If the table has no users, the response is `404 Not Found`:

```json
{
	"message": "No users found!"
}
```

If you are running the API locally, replace `8080` with `5000` in the `curl`
commands.
