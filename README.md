# GameDevServer2025
Backend для финалистов GameDev NTO 2025

Бекенд от организаторов постоянно лежал, нам для разработки нужен был рабочий сервер. Этот сервер в точности повторяет оригинальный сервер

Вы можете создать pr либо написать issue, если вы хотите внести правки в API

Стек: Django, djangorestframework


# Как запустить?

with docker
```
docker build -t gamedevserver .
docker run -p 8000:8000 gamedevserver
```


without docker
```
python3 -m pip install -r requirements.txt
cd gamedevserver
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```


Теперь отправляйте запросы на 127.0.0.1:8000


# Как получить UUID игры? (Важно)

Этот пункт отличается от предоставленного в оригинальном API
Вам достаточно сделать POST запрос на /api/games/ чтобы получить UUID игры 

Пример запроса на python:
```python
import requests
print(requests.post("http://127.0.0.1:8000/api/games/").text)
{"team_name":"some_team","uuid":"5ccfcba5-5cdb-4025-9d17-8bcd87986c2e"}
```



