 FastAPI КР4 

Инструкции по запуску проекта:

1) Создайте виртуальное окружение и установите зависимости:


python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


2) Настройка окружения (необязательно): скопируйте .env.example в .env

3) Запустить приложение:


uvicorn app.main:app --reload


4) Запустить тесты:


pytest -q


Миграции Alembic находятся в папке alembic/. По умолчанию используется база данных sqlite:///./test.db.
