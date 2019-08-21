#!/usr/bin/env bash

docker run --name mysql -e MYSQL_ROOT_PASSWORD=pw \
                        -e MYSQL_DATABASE=weather \
                        -e MYSQL_USER=weather \
                        -e MYSQL_PASSWORD=weather \
                        -d mysql

#echo "CREATE USER 'weather'@'localhost' IDENTIFIED BY 'weather'" | mysql -uroot -ppw

#echo "CREATE DATABASE weather" | mysql -uroot -ppw

#echo "GRANT ALL PRIVILEGES ON weather.* TO 'weather'@'localhost'" | mysql -uroot -ppw
