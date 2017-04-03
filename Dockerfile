# Use this as a base image
FROM ubuntu:16.04

# Maintainer Info
MAINTAINER Ricardo Lobo <ricardolobo@soloweb.pt>

# set default environment
ENV APP_IN_PRODUCTION=false

# update repos and install
# pip3, supervisor, nginx
# python postgres adapter
# and gettext to provide
# i18n translation support
RUN apt-get update && \
apt-get -y install \
python3-pip \
supervisor \
nginx \
python3-psycopg2 \
gettext

# copy code to image
COPY . /var/www/

# set the working directory
WORKDIR /var/www/

# install django and django dependencies using pip3
RUN pip3 install -r /var/www/dist/requirements.txt

# make init script executable
RUN chmod ug+x /var/www/dist/initialize.sh

# remove nginx default site
RUN rm /etc/nginx/sites-enabled/default

# copy supervisor configuration
COPY ./dist/api.conf /etc/supervisor/conf.d/api.conf

# default command
CMD ["/usr/bin/supervisord"]
