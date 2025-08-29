# mock-rest-api

### Установить Flask
    pip install flask

### Установить openssl
    apt install openssl

### Сгенерировать сертификат и ключ
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

### Запустить мок-сервер
    python3 app.py


### Добавить сертификаты в клиент