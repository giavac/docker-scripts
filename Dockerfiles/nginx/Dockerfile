FROM ubuntu:14.04

MAINTAINER Giacomo Vacca "giacomo.vacca@gmail.com"

ENV REFRESHED_AT 2016-01-04

RUN apt-get update \
    && apt-get -y -q install nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/www/html

COPY nginx/global.conf /etc/nginx/conf.d/
COPY nginx/nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /etc/nginx/ssl
# Expect from volume:
# /etc/nginx/ssl/nginx.crt
# /etc/nginx/ssl/nginx.key
# openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt -subj "/C=XX/ST=XXXX/L=XXXX/O=XXXX/CN=localhost"

EXPOSE 80
EXPOSE 443

CMD nginx

##########################################
# Build:
### docker build -t gvacca/nginx_ssl .

# Run:
### docker run -d -p 8443:443 -v $PWD/website/:/var/www/html/website/ -v $PWD/nginx/ssl/:/etc/nginx/ssl/ gvacca/nginx_ssl

# Run inside a docker network:
### docker run -d --net=http_network --name=nginx_ssl -v $PWD/website/:/var/www/html/website/ -v $PWD/nginx/ssl/:/etc/nginx/ssl/ gvacca/nginx_ssl
