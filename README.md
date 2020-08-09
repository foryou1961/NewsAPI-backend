# Что это?
Это REST API для новостного блога.

## Запуск сервиса локально
1. Устновить вертуальное окружение и зависимости:
    ```bash
    python3 -m venv env
    pip install -r requirements/requirements-dev.txt
    ```

2. Создать файл .env аналогичный .env.example и заполнить его.

3. Создаем пользователя и базу в PostgreSQL:
    ```shell script
    sudo -u postgres psql
    
    # Выполняем запросы в консоли СУБД
    CREATE DATABASE <имя_базы>;
    CREATE USER <имя_пользователя> WITH PASSWORD '<ваш_пароль>';
    GRANT ALL PRIVILEGES ON DATABASE <имя_базы> TO <имя_пользователя>;
    ALTER USER <имя_пользователя> WITH CREATEDB;
    ```

4. Миграция базы данных
    ```bash
    python manage.py migrate
    ```

5. Запуск сервиса локально

    ```bash
    python manage.py runserver
    ```

## Тестирование
Для запуска тестов необходимо указать путь к файлу
   
```shell script
pytest tests/types/test_types.py -s -vv
```   
