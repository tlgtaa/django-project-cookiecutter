#!/bin/bash

set -e

python /proj/hooks/connectpg.py "$DATABASE_URL" && exec "$@"
