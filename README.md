# Установка

# Зависимости

 - [Docker](https://docs.docker.com/install/) 17.06.0+
 - [docker-compose](https://docs.docker.com/compose/overview/) последняя версия
 - [Python 3](https://www.python.org/)
 - [rsa ключ для доступа к шифрованным данным](./docs/gpg.md)
 - доступ к серверу с резервными копиями

## Настройка окружения
* [Local](./docs/configure/local.md)
* [Production](./docs/configure/production.md)


### Шифрованные данные
Для каждого окружения есть шифрованный файл в котором хранятся секретные данные.

 - local -> `./etc/env/.env.local.gpg`
 - production -> `./etc/env/.env.production.gpg`

Детали по работе с ними [тут](./docs/gpg.md)

### Изображение
Для локального окружения запрос к изображениям проксируется на сайт `politsturm.com`.
