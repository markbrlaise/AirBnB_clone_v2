#!/usr/bin/env bash

# update system and install ngnix
sudo apt-get -y update
sudo apt-get -y install nginx

# allow http traffic on nginx
ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/

echo 'hola mate'>/data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "47i\tlocation /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default

sudo service nginx restart
