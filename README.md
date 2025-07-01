# Weekly Status Generattor

Writing weekly status mails isn't a task which most people look forward too. It's a sample project which will take and manage daily logs for you and use an LLM to generate the email body for you.

## Note: For now it's a tool which developers can run locally on their system, hence there is not authentication/authorization done. Anyone using this tool will have access to all the tasks 🫶

## LLM info
This tool uses phi3:3.8b LLM https://ollama.com/library/phi3 the model runs locally on the server and hence is completely free. The performance of the LLM will depend on the machine running it. The model was chosen because it was lightweight and has been found good for the tasks of summarization. Reddit post which helped coming to conclusion: https://www.reddit.com/r/LocalLLaMA/comments/1dnavrt/update_model_review_for_summarizationinstruct_1gb/

## Setup:
Populate the .env file using the template provided in .env-template

## Running locally
Run below command to run locally
```
docker compose up --build
```

### Run migrations
```
docker exec weekly-status-django-container python manage.py makemigrations
docker exec weekly-status-django-container python manage.py migrate
```
Run after changes in db schema

## Helpful commands
1. Interact with shell of docker containers
    ```
    docker exec -it container-name command
    ```
    `-it` = shell will be interactive
    
    For example to connect with the postgresql container and interact with db

    ```
    docker exec -it weekly-status-db-container psql -U db_user -d db_name
    ```