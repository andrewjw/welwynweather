#!/bin/bash

set -e

npm install

npx next info

npm run build

kill `cat pid.txt` || true

nohup npm run start > logs/weather.log 2>&1 < /dev/null &

echo "$!" > pid.txt
