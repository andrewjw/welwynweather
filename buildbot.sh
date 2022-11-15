#!/bin/bash

set -e

npm install

npx next info

npx next lint

BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$BRANCH" == "master" ]]; then
  ssh $SSH_USER@$SSH_HOST "cd /var/www/www.welwynweather.co.uk/weather; git pull; ./run_prod.sh"
fi
