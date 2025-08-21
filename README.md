<p align="center">
  <a href="#"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>
<p align="center">
<a href="" target="_blank">
    <img src="https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg" alt="Coverage">
</a>
<a href="" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

# ⚡ các câu lệnh cài đặt 

## 1. install fastapi

```bash
  pip install "fastapi[standard]"
```

## 2. play fastapi

```bash
  fastapi dev src/main.py
```

```bash
  farm uvicon main:app --reload
```

# Stop container hiện tại
```
   docker-compose down
```

# Rebuild image
```
   docker-compose build --no-cache
```

# Start lại
```
   docker-compose up -d
```

# Kiểm tra logs
```
   docker-compose logs -f app
```

# source code

```
├── .env
├── Dockerfile.web
├── README.md
├── __pycache__
    └── main.cpython-313.pyc
├── boot
    └── docker-run.sh
├── compose.yaml
├── nbs
    └── hello-world.ipynb
├── requirements.txt
└── src
    ├── __pycache__
        └── main.cpython-313.pyc
    ├── api
        ├── __init__.py
        ├── __pycache__
        │   └── __init__.cpython-313.pyc
        └── events
        │   ├── __init__.py
        │   ├── __pycache__
        │       ├── __init__.cpython-313.pyc
        │       └── routing.cpython-313.pyc
        │   └── routing.py
    └── main.py
```