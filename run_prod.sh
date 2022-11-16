#!/bin/bash

set -e

npm install

npx next info

npm run build

kill `cat pid.txt`

npm run start &

echo "$!" > pid.txt
