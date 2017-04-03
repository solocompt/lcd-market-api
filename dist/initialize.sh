#!/bin/bash

# copy and enable nginx virtual host configuration
cp ./dist/api /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/api /etc/nginx/sites-enabled/api

# in development mode
if [ "$APP_IN_PRODUCTION" != "true" ]; then
    # migrations are automatic
    python3 /var/www/manage.py migrate --noinput
    # static files are collected on container init
    python3 /var/www/manage.py collectstatic --noinput
fi

exit 0