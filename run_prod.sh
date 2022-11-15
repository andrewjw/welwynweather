#!/bin/bash

set -e

npm install

npx next info

npm run build

killall node

npm run start &
