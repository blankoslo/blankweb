# Readme

### Utviklingsmiljø

- Kan være greit å bruke venv: http://docs.python-guide.org/en/latest/dev/virtualenvs/
- Start devserveren slik: ```python manage.py runserver```
- Migreringer gjøres med ```python manage.py makemigrations``` og ```python manage.py migrate```
- .env fil i rot må inneholde DATABASE_URL, DEBUG, GOOGLE_STORAGE_USER, GOOGLE_STORAGE_KEY og GOOGLE_STORAGE_BUCKET

- Migrere på heroku: ```heroku run python manage.py migrate```
