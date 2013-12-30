#!/bin/bash

if [ ! -f "/usr/sbin/nginx" ];
then
    apt-get install nginx -y
fi

if [ ! -f "/usr/bin/git" ];
then
    apt-get install git -y
fi

if [ ! -d "/root/michchap" ];
then
    cd /root; git clone https://github.com/michaeltchapman/michchap
fi

cd /root/michchap
git pull

cp /root/michchap/deploy/resume /etc/nginx/sites-enabled/resume
cp /root/michchap/deploy/mime.types /etc/nginx/mime.types
service nginx restart

python repoparse.py > /usr/share/nginx/www/resume/index.html
cp -r static/* /usr/share/nginx/www/resume

