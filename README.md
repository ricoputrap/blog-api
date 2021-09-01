# Blog API

Backend service for my project: **Blog Web App**


## Tech Stack

**Server:** `Python`, `Flask`, `Flask-RESTful`, `Flask-SQLAlchemy`, `flask-marshmallow`, `Flask-Migrate`

**Database:** PostgreSQL (`psycopg2-binary`)


## Run Locally

Clone the project

```bash
  git clone https://github.com/ricoputrap/blog-api
```

Go to the project directory
```bash
  cd blog-api
```

Prepare & activate virtual environment
```bash
  python -m venv env
  source env/bin/activate
```

Install dependencies
```bash
  pip install -r requirements.txt
```

Copy and adjust `.env.example` to `.env`.

Run the docker container
```bash
  docker-compose up -d
```

Open PostgreSQL database CLI on your docker container
and create a new table with the name you wrote 
in the variable `POSTGRES_DB` in the `.env` file of your project

Start the server
```bash
  python3 wsgi.py
```

On your project root directory, initialize your db
```bash
  flask db init
```

Make migration scripts for your db models
```bash
  flask db migrate -m "Initial migration"
```

Run the latest version of db migration file
```bash
  flask db upgrade
```