# Настройка локального окружения

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
    
    Вы так же можете ознакомиться с  [переопределением переменных окружения](../env_override.md)
    
    Для просмотра обозначений ключей используем `--help`

4. Настраиваем [proxy](./docs/proxy.md)

5. Сайт будет доступен по адресу `http://politsturm.local`

    Данный домен прописан в переменных окружения и используется как `WP_SITEURL` и `WP_HOME`

Админка: http://politsturm.local/wp-admin/index.php

Авторизация: http://politsturm.local/wp-login.php