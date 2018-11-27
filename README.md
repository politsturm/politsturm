# Установка

# Зависимости

 - [Docker](https://docs.docker.com/install/) 17.06.0+
 - [docker-compose](https://docs.docker.com/compose/overview/) последняя версия
 - [Python 3](https://www.python.org/)
 - [rsa ключ для доступа к шифрованным данным](./docs/gpg.md)
 - доступ к серверу с резервными копиями

## Локальное окружение

1. Не фиксируем права доступа
    ```bash
    git config core.fileMode false
    ```

2. Делаем скрипты исполняемыми

    ```
    sudo chmod +x ./etc/scripts/*
    ```

3. Запускаем сборку
    ```bash
    ./etc/scripts/init_local -r -f
    ```

    Для просмотра обозначений ключей используем `--help`

4. Настраиваем [proxy](./docs/proxy.md)

5. Сайт будет доступен по адресу `http://politsturm.local`

    Данный домен прописан в переменных окружения и используется как `WP_SITEURL` и `WP_HOME`

### Шифрованные данные
Для каждого окружения есть шифрованный файл в котором хранятся секретные данные.

 - local -> `./etc/env/.env.local.gpg`
 - production -> `./etc/env/.env.production.gpg`

Детали по работе с ними [тут](./docs/gpg.md)

### Изображение
Для локального окружения запрос к изображениям проксируется на сайт `politsturm.com`.
