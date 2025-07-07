# ✅ GitHub Actions를 사용해 Django 프로젝트의 테스트 자동화(CI)를 설정

```yml
name: Django CI

on:
  push:
    branches: [ "main", "dev" ]
  pull_request:
    branches: [ "main", "dev" ]

jobs:
  build:
    runs-on: ubuntu-latest

    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_ROOT_PASSWORD: root
          MYSQL_DATABASE: restaurant_db
          MYSQL_USER: restaurant_user
          MYSQL_PASSWORD: db_password
        ports:
          - 3306:3306
        options: >-
          --health-cmd="mysqladmin ping --silent"
          --health-interval=10s
          --health-timeout=5s
          --health-retries=5

    strategy:
      matrix:
        python-version: [3.12.3]

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install system dependencies for mysqlclient
      run: sudo apt-get install -y default-libmysqlclient-dev

    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run migrations
      run: python manage.py migrate

    - name: Run Tests
      env:
        DB_NAME: restaurant_db
        DB_USER: root
        DB_PASSWORD: root
        DB_HOST: 127.0.0.1
      run: python manage.py test --verbosity=2
```


# ✅ settings.py 내 DATABASES 설정

```
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'restaurant_db'),
        'USER': os.environ.get('DB_USER', 'restaurant_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'db_password'),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}
```

# ✅ .env 파일 예시 (로컬 테스트 시 사용)

```
DB_NAME=restaurant_db
DB_USER=restaurant_user
DB_PASSWORD=db_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

# ✅ requirements.txt 에 포함되어야 할 패키지 예시
```
Django>=5.1
mysqlclient>=2.2
python-dotenv>=1.0
pytest-django>=4.5
```

# ✅ manage.py 또는 wsgi.py 상단에 dotenv 설정 추가 (로컬 개발용)
```
import dotenv
import os

dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
```

# ✅ 최소 테스트 코드 예시 (ex. app/tests.py)
```
from django.test import TestCase

class SmokeTest(TestCase):
    def test_base_case(self):
        self.assertEqual(1 + 1, 2)
```
