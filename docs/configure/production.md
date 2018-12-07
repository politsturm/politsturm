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
    INIT_WP_HONE=https://politsturm.com INIT_WP_SITEURL=https://politsturm.com ./etc/scripts/init_production -f
    ```
    
    Вы так же можете ознакомиться с  [переопределением переменных окружения](../env_override.md)

    Для просмотра обозначений ключей используем `--help`
    
4. Далее вам необходимо настроить веб сервер, что бы он смотрел внутрь nginx контенера