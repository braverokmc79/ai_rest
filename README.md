# Django 웹 프로그래밍 강좌 정리

본 강좌는 Django를 활용한 웹 프로그래밍을 배우기 위한 기초 강좌로, 프로젝트 생성부터 Git 사용법, 데이터베이스 모델링, Django View 및 Form, 테스트 작성, 정적 파일 관리, Admin 커스터마이징 등을 다룹니다.


### 파이썬·장고 웹개발 | 코담 - 코드에 세상을 담다

[![코담 소개 이미지](https://codam.kr/assets/images/og-image.jpg)](https://codam.kr/)

---



## 📦 AI Restaurant Backend




### 🔖 환경 변수 설정

**`.env`**

```bash
ENV=dev
```

**`.env.dev`**

```bash
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True

# MySQL
DATABASE=mysql
DB_ENGINE=mysql
DB_NAME=ai_restaurant
DB_USER=ai_restaurant
DB_PASSWORD=ai_restaurant
DB_HOST=db
DB_PORT=3306
```

---

### 🐳 Docker Compose 실행 방법

1️⃣ **도커 이미지 빌드**
최초 실행 시 또는 코드 변경 후 이미지를 다시 빌드하려면:

```bash
docker compose build
```

캐시 없이 강제로 새로 빌드하려면:

```bash
docker compose build --no-cache
```

2️⃣ **도커 컨테이너 실행**

```bash
docker compose up
```

백그라운드 실행 (detached mode):

```bash
docker compose up -d
```

3️⃣ **컨테이너 중지**

```bash
docker compose down
```

---

### 👤 Django 슈퍼유저 생성

도커 컨테이너가 실행 중일 때 다음 명령어로 Django 백엔드 컨테이너에 접속합니다:

```bash
docker exec -it ai_rest_backend bash
```

컨테이너 내부에서 Django 명령어 실행:

```bash
python manage.py createsuperuser
```

프롬프트에 따라 사용자 이름, 이메일, 비밀번호를 입력하면 됩니다.

---

### 📋 도커 컨테이너 관리

#### ✅ 실행 중인 컨테이너 확인

```bash
docker ps
```

#### ✅ 모든 컨테이너 확인 (중지된 것도 포함)

```bash
docker ps -a
```

#### ✅ 특정 컨테이너 로그 보기

```bash
docker logs ai_rest_backend
```

---

### 🛠 컨테이너에 접속하기

**백엔드 컨테이너 접속:**

```bash
docker exec -it ai_rest_backend bash
```

**DB(MySQL) 컨테이너 접속:**

```bash
docker exec -it ai_restaurant_db bash
```

---

### 🌐 개발 서버 접속

컨테이너 실행 후 브라우저에서 접속:

```
http://localhost:8000
```

관리자 페이지:

```
http://localhost:8000/admin/
```
