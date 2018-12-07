# Переопределение переменных окружения

Так же при запуске скрипта `./etc/scripts/init` можно переопределить переменные окружения в .env файле указав
необходимые переменные окружения с префиксом `INIT_`.
Это работает со скриптами `./etc/scripts/init_*` т.к. каждый из них вызывает `./etc/scripts/init`

```bash
    INIT_WP_HOME=http://politsturm.mylocal INIT_WP_SITEURL=http://politsturm.mylocal ./etc/scripts/init_local
    INIT_WP_HOME=http://politsturm.mylocal INIT_WP_SITEURL=http://politsturm.mylocal ./etc/scripts/init
```

В данном примере скрипты выполнились с переопределенными переменными окружения `WP_HOME` и `WP_SITEURL`