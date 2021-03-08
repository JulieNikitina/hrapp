# hrapp
Приложение для учета выполнения тестовых заданий соискателями на различные должности.

## Инструкция по развертыванию приложения на сервере.
Данная инструкция позволит развернуть приложение HRapp на сервере

### Настройка сервера
* Подключитесь к удаленному серверу
* Обновите индекс пакетов APT 
  ```sudo apt update ```
* Обновите установленные в системе пакеты и установите обновления безопасности  
  ```sudo apt upgrade -y ```
* Установите менеджер пакетов pip, утилиту для создания виртуального окружения venv, систему контроля версий 
  ```git sudo apt install python3-pip python3-venv git -y``` 
* Клонируйте репозиторий с проектом 
  ```https://github.com/JulieNikitina/hrapp.git```
### Подготовка проекта
* Перейдите в директорию с проектом
  ``` cd cd hrapp/ ```
* Создайте .env файл 
  ```nano <имя-пользователя-в-системе>/<директория-проекта>/hr_app/.en```
* Укажите в .env файле следующие параметры
```
  SECRET_KEY=<укажите secret_key>
  IS_DEV=false
  SERVER_HOST=<ваш-ip>
```
  
* Активируйте виртуальное окружение и установите зависимости
  ```python3 -m venv venv```
  ```. venv/bin/activate```
  ```python -m pip install -r requirements.txt ```
  
### Подключение базы данных Postgres
* Установите необходимые для работы PostgreSQL пакеты
  ```sudo apt install postgresql postgresql-contrib -y```
  
* Установите настройки локализации
  ```
  sudo update-locale LC_ALL=<пробел>
  sudo update-locale LC_CTYPE=ru_RU.UTF-8
  sudo update-locale LC_COLLATE=ru_RU.UTF-8
  ```
* Создайте базу данных и пользователя
  ```sudo -u postgres psql
     CREATE DATABASE <имя_бд>;
     CREATE USER <имя_пользователя> WITH ENCRYPTED PASSWORD <'пароль'>; 
      GRANT ALL PRIVILEGES ON DATABASE <имя_бд> TO <имя_пользователя>;  
      exit```
* Внесите в .env файл данные о базе данных
  ```nano <имя-пользователя-в-системе>/<директория-проекта>/hr_app/.en```
  ```DATABASE_URL=psql://<имя_пользователя_бд>:<'пароль'>@127.0.0.1:5432/<имя_бд>```
  
* Выполните миграции
  ```python manage.py makemigration```
  ```python manage.py migrate```
  
### Создание юнита Gunicorn
* Cоздайте и откройте в nano файл gunicorn.service в директории /etc/systemd/system/
  ```sudo nano /etc/systemd/system/gunicorn.service```
  
  ```
    [Unit]
  Description=gunicorn daemon
  After=network.target
  [Service]
  User=<имя-пользователя-в-системе>
  WorkingDirectory=/home/<имя-пользователя-в-системе>/<директория-проекта>
  ExecStart=/home/<имя-пользователя-в-системе>/<директория-проекта>/venv/bin/gunicorn  --bind 127.0.0.1:8000 --error-logfile /home/<имя-пользователя-в-системе>/<директория-проекта>/error.log  hr_app.wsgi:application

    [Install]
  WantedBy=multi-user.target
  ```
* Запустите gunicorn-deamon
  ``` sudo systemctl start gunicorn```
* Включите  gunicorn в список автозапуска операционной системы
  ``` sudo systemctl enable gunicorn```
### Подключение NGINX
* Установите nginx
  ```sudo apt install nginx -y```
* Настройте файерволл
  ```
  sudo ufw allow 'Nginx Full'
  sudo ufw allow OpenSSH 
  sudo ufw enable 
  ```
* Запустите nginx
  ```sudo systemctl start nginx``` 
* Выполните команду
  ```python manage.py collectstatic ```
* Измените конфигурационный файл nginx
  ```sudo nano /etc/nginx/sites-enabled/default```
```
server {
    listen 80;
    server_name http://<ваш-ip>;

    location /static/ {
        root /home/<имя-пользователя-в-системе>/<директория-проекта>;
    }
    location /media/ {
        root /home/<имя-пользователя-в-системе>/<директория-проекта>;
    }
    location / {
        include proxy_params;
        # передавать запросы нужно на внутренний IP на порт 8000
        proxy_pass http://127.0.0.1:8000;
    }
 }
 ```
* Перезапустите nginx 
  ```sudo nginx -s reload```
 
* В браузере перейдите по вашему IP для дальнейшей работы с приложением
  
 ## Работа с приложением
 
* Создайте суперпольователя для администрирования приложения
``` python manage.py createsuperuser```

* Перейдите на <IP>/admin/

* В рамках работы с административный интерфейсом приложения предусматривается следующий функционал:
  - создание пользователя 
  - создание роли пользователя (должность), должность руководителя создается первой с pk 1
  - создание подразделений подразделение HR создается первым с pk 1
  - создание "сотрудника": пользователя, связанного с моделями "роль" и "отдел"
 
* В рамках работы с интерфейсом приложения:
  - сотрудник отдела hr (вне зависимости от роли) может добавлять новую запись о соискателе и исправлять внесенные данные
  - руководитель отдела может принять результат тестового задание от соискателя и внести дату получения результата
  - пользователь может самостьятельно изменить свой пароль

## При создании приложения использовано:
  * [Python: 3.8.5](https://www.python.org/)
  * [Django: 3.0.8](https://www.djangoproject.com/)
  * [PostgreSQL: 12.4](https://www.postgresql.org/)
  * [Docker: 3.1.0](https://www.docker.com/)
  * [gunicorn: 20.0.4](https://gunicorn.org/)
### Aвтор проекта
  Никитина Юлия - [GitHub](https://github.com/JulieNikitina)
### Лицензия
[MIT](https://choosealicense.com/licenses/mit/)