#!/bin/bash

set -e

npm install

npx next info

npx next lint

npx next build