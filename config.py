class config_Globals:

       cmd = [
           ' status',
           ' start',
           ' reload',
           ' stop'
       ]

       services = [
           'nginx',
           'mysql',
           'php7.2-fpm'
       ]

       welcome_text = {
           "text": "LEMP Manager!",
           "font": "slant"
       }

       load = {
           "text": "Loading",
           "spinner": "dots"
       }

       logs = {
           "nginx-access": "/var/log/nginx/access.log",
           "nginx-error": "/var/log/nginx/access.log",
           "mysql-error": "/var/log/mysql/error.log",
           "php": "not configured yet"
       }

