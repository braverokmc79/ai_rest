폴더명: AIRestaurant
git링크:[https://github.com/handgonpo/AIRestaurant](https://github.com/handgonpo/AIRestaurant)
```bash
mkdir AIRestaurant
cd AIRestaurant
python -m venv venv
source venv/bin/activate
pip install django
pip install django djangorestframework
pip install black isort flake8 pre-commit # 개발도구
pip install pytest pytest-django coverage # 테스트도구
pip install django-environ ipython rich # 기타편의도구
pip install Pillow
pip freeze > requirements.txt

django-admin startproject proj .
python manage.py startapp restaurant
```

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'restaurant',
]
```

`.pre-commit-comfig.yaml` 설정 파일 생성
```python
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer

  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        args: ["--profile", "black"]

  # - repo: https://github.com/pycqa/flake8
  #  rev: 7.0.0
  #  hooks:
  #    - id: flake8
  #      args: [--max-line-length=92]
```

`pre-commit` 초기화 및 Git에 연결
```bash
pip install pre-commit
pre-commit install

git init .
pre-commit install
```

```bash
git remote add origin https://github.com/handgonpo/AIRestaurant.git
git branch -M main
```

![[Pasted image 20250706195250.png]]

![[Pasted image 20250706195325.png]]

Actions 추가 : django-test.yml 을 작성한다.
```yaml
name: Django CI

on:
  push:
    branches: [ "main","dev" ] # dev추가
  pull_request:
    branches: [ "main","dev" ] # dev추가

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.12.3] # 자신의 버전과 맞추기 python --version

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5 # 신버전으로 올리기
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run Tests
      run: |
        python manage.py test

```

![[Pasted image 20250706140403.png]]

![[Pasted image 20250706140528.png]]

서버 실행
```bash
python manage.py runserver
```
