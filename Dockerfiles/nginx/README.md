# Build and run a docker container with nginx

## Build
```docker build -t gvacca/nginx .```

## Run
```docker run -d -p 8443:443 -p 8080:80 -v $PWD/website/:/var/www/html/website/ -v $PWD/nginx/ssl/:/etc/nginx/ssl/ gvacca/nginx```

`$PWD/website` is expected to contain the server website.
`$PWD/nginx/ssl` is expected to contain the SSL certs

## Run inside an existing network, e.g. 'http_network'
```docker run -d --net=http_network --name=nginx_ssl -v $PWD/website/:/var/www/html/website/ -v $PWD/nginx/ssl/:/etc/nginx/ssl/ gvacca/nginx```

## Generate self-signed SSL certs
```openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt -subj "/C=XX/ST=XXXX/L=XXXX/O=XXXX/CN=localhost"```

They are expected at `$PWD/nginx/ssl/`
