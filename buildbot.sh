#!/bin/bash

set -e

npm install

npx next info

npx next lint

npm run build