#!/bin/bash

source /opt/venv/bin/activate

cd /code
RUN_PORT=${PORT:-8002}  # Lấy từ biến môi trường hoặc default 8002
RUN_HOST=${HOST:-0.0.0.0}

gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT main:app