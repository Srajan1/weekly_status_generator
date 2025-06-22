# Weekly Status Generattor

Writing weekly status mails isn't a task which most people look forward too. It's a sample project which will take and manage daily logs for you and use an LLM to generate the email body for you.

## Setup:
Populate the .env file using the template provided in .env-template

## Running locally
Run below command to run locally
```
docker compose up --build
```

### Run migrations
```
docker compose exec django-web python manage.py makemigrations
docker compose exec django-web python manage.py migrate 
```
Run after changes in db schema
