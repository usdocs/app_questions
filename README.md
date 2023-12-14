# Сервис выдачи вопросов для викторины
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=5fe620)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=5fe620)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=ffffff&color=5fe620)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=ffffff&color=5fe620)](https://www.docker.com/)
[![Gunicorn](https://img.shields.io/badge/-Gunicorn-464646?style=flat&logo=Gunicorn&logoColor=ffffff&color=5fe620)](https://gunicorn.org/)
[![nginx](https://img.shields.io/badge/-nginx-464646?style=flat&logo=nginx&logoColor=ffffff&color=5fe620)](https://nginx.org/)

## Описание

Данный проект:
- Принимает на вход POST запросы с содержимым вида {"questions_num": integer} ;
- После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов;
- Далее, полученные ответы сохраняются в базе данных, а именно следующая информация: 
     1. **ID вопроса**
     2. **Текст вопроса** 
     3. **Текст ответа**
     4. **Дата создания вопроса**

- В случае, если в БД имеется такой же вопрос, к публичному API с викторинами выполняются дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
- Ответом на запрос является предыдущий сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

## Стек технологий:
- Python 3
- Django 3.2
- Django ORM
- DRF (Django REST framework)
- Gunicorn
- nginx
- Docker
- Docker-compose
- PostgreSQL
- GIT

## Шаблон наполнения .env
```
# указываем, с какой БД работаем
DB_ENGINE=django.db.backends.postgresql
# имя базы данных
DB_NAME=
# логин для подключения к базе данных
POSTGRES_USER=
# пароль для подключения к БД
POSTGRES_PASSWORD=
# название сервиса (контейнера)
DB_HOST=
# порт для подключения к БД
DB_PORT=
# секретный ключ Django
SECRET_KEY=
```

## Автоматизация развертывания серверного ПО
Для автоматизации развертывания ПО на боевых серверах используется среда виртуализации Docker, а также Docker-compose - инструмент для запуска многоконтейнерных приложений. Docker позволяет «упаковать» приложение со всем его окружением и зависимостями в контейнер, который может быть перенесён на любую Linux -систему, а также предоставляет среду по управлению контейнерами. Таким образом, для разворачивания серверного ПО достаточно чтобы на сервере с ОС семейства Linux были установлены среда Docker и инструмент Docker-compose.

## Описание команд для запуска приложения в контейнерах
Для запуска проекта в контейнерах используем **docker-compose** : ```docker-compose up -d --build```, находясь в директории (infra) с ```docker-compose.yaml```

После сборки контейнеров выполяем:
```bash
# Выполняем миграции
docker-compose exec web python manage.py migrate
# Создаем суперппользователя
docker-compose exec web python manage.py createsuperuser
# Собираем статику со всего проекта
docker-compose exec web python manage.py collectstatic --no-input
```

**Пример POST-запроса:**
<br>
URL: `http://127.0.0.1:8000/api/v1/questions/`
<br>
Request body: `{questions_num: 100}`
<br>
Response: "Question"

#### Разработчик проекта

Автор: Andrey Balakin  
E-mail: [usdocs@ya.ru](mailto:usdocs@ya.ru)
