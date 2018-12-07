# Проксирование запросов в Docker контейнер (Unix + Nginx)

1. Добавить доменное имя в hosts (Только если вы не используете DNS сервер)

Файл /etc/hosts

```
127.0.0.1       politsturm.local

```

2. Настраиваем nginx 

Создаем файл /etc/nginx/conf.d/proxy.conf со следующим содержимым
```

server
{
    listen 80;

    server_name politsturm.local;

    location /
    {
        proxy_pass http://127.0.0.1:8011;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

```
