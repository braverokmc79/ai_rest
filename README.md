# Django 웹 프로그래밍 강좌 정리

본 강좌는 Django를 활용한 웹 프로그래밍을 배우기 위한 기초 강좌로, 프로젝트 생성부터 Git 사용법, 데이터베이스 모델링, Django View 및 Form, 테스트 작성, 정적 파일 관리, Admin 커스터마이징 등을 다룹니다.


### 파이썬·장고 웹개발 | 코담 - 코드에 세상을 담다

[![코담 소개 이미지](https://codam.kr/assets/images/og-image.jpg)](https://codam.kr/)

---


# 🚀 AI REST Backend 프로젝트 README

## 📦 Docker Compose 실행 방법

1. **Docker 이미지 빌드 및 컨테이너 실행**

   ```bash

   docker compose up --build --no-cache


  # 클린하게 전체 재시작
   docker compose down --volumes --remove-orphans
   docker compose up --build --no-cache

   ```




   * `--build` 옵션은 변경된 코드로 이미지를 다시 빌드합니다.
   * 백그라운드 실행하려면:

     ```bash
     docker compose up -d
     ```

2. **컨테이너 상태 확인**

   ```bash
   docker ps
   ```

3. **컨테이너에 접속하기 (bash)**

   ```bash
   docker exec -it ai_rest_backend bash
   ```


---


.env 시크릿 키 생성
``` 
# Linux/macOS Bash 환경 (UUID 기반)

openssl rand -hex 32

```



---

## 🛠 슈퍼유저 생성 방법

1. 컨테이너에 접속:

   ```bash
   docker exec -it ai_rest_backend bash
   ```

2. Django migrate 실행 (최초 실행 시)

   ```bash
   python manage.py migrate
   ```

3. 슈퍼유저 생성:

   ```bash
   python manage.py createsuperuser
   ```

---

## 🔖 환경변수 설정

### .env

```
ENV=dev
```

### .env.dev

```
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

## ⚠️ Windows에서 entrypoint.sh CRLF 문제 해결

Windows에서는 `entrypoint.sh` 파일의 줄바꿈이 `CRLF`로 저장되면 컨테이너 실행 시 오류가 발생합니다:

```
bash: ./entrypoint.sh: /bin/bash^M: bad interpreter
```

### ✅ 해결 방법

1. **Git 설정 변경 (권장)**

   ```bash
   git config --global core.autocrlf input
   ```

2. **이미 변경된 파일 수정**

   * VSCode에서 오른쪽 아래 `CRLF` 클릭 → `LF` 선택 → 저장
   * CLI에서 한 번에 수정:

     ```bash
     sed -i 's/\r$//' entrypoint.sh
     ```

3. **`.gitattributes`로 고정 (추가 권장)**

   `.gitattributes` 파일에 아래 내용 추가:

   ```gitattributes
   *.sh text eol=lf
   ```

   이 설정은 `.sh` 파일을 항상 LF로 유지합니다.

---

## 📂 기타 유용한 명령어

* 로그 확인:

  ```bash
  docker compose logs -f
  ```
* 컨테이너 중지:

  ```bash
  docker compose down
  ```

---



## DBeaver에서 Docker MySQL 접속 방법

당신의 `docker-compose.yml` 설정 기준으로, MySQL 컨테이너는 다음과 같이 구성되어 있습니다:

```yaml
db:
  image: mysql:8.3
  container_name: ai_restaurant_db
  environment:
    MYSQL_ROOT_PASSWORD: rootpass123
    MYSQL_DATABASE: ai_restaurant
    MYSQL_USER: ai_restaurant
    MYSQL_PASSWORD: ai_restaurant
  ports:
    - "3305:3306"
```

이 설정에 따라 DBeaver에서 접속하기 위한 정보는 다음과 같습니다.

---

### ✅ DBeaver 접속 정보

| 항목       | 값                          |
| -------- | -------------------------- |
| DB 타입    | MySQL                      |
| Host     | `127.0.0.1` 또는 `localhost` |
| Port     | `3305` (외부 포트)             |
| Database | `ai_restaurant`            |
| User     | `ai_restaurant`            |
| Password | `ai_restaurant`            |

---



## DBeaver에서 Docker MySQL 접속 방법

당신의 `docker-compose.yml` 설정 기준으로, MySQL 컨테이너는 다음과 같이 구성되어 있습니다:

```yaml
db:
  image: mysql:8.3
  container_name: ai_restaurant_db
  environment:
    MYSQL_ROOT_PASSWORD: rootpass123
    MYSQL_DATABASE: ai_restaurant
    MYSQL_USER: ai_restaurant
    MYSQL_PASSWORD: ai_restaurant
  ports:
    - "3305:3306"
```

이 설정에 따라 DBeaver에서 접속하기 위한 정보는 다음과 같습니다.

---

### ✅ DBeaver 접속 정보

| 항목       | 값                          |
| -------- | -------------------------- |
| DB 타입    | MySQL                      |
| Host     | `127.0.0.1` 또는 `localhost` |
| Port     | `3305` (외부 포트)             |
| Database | `ai_restaurant`            |
| User     | `ai_restaurant`            |
| Password | `ai_restaurant`            |

---

### ✅ DBeaver 접속 절차

1. DBeaver 실행
2. 좌측 상단 `Database > New Database Connection` 클릭
3. DB 종류 선택: `MySQL`
4. "Next" 클릭
5. 아래 정보 입력:
   - **Server Host**: `127.0.0.1`
   - **Port**: `3305`
   - **Database**: `ai_restaurant`
   - **Username**: `ai_restaurant`
   - **Password**: `ai_restaurant`
6. `Test Connection` 클릭해서 연결 확인
7. 성공하면 "Finish"

---

### ⚡ 접속 안 될 경우 점검 사항

- **컨테이너가 실행 중인지 확인**

  ```bash
  docker ps
  ```

  MySQL 컨테이너(`ai_restaurant_db`)가 떠 있어야 함

- **포트 충돌 여부 확인** 로컬에 다른 MySQL이 `3305`나 `3306`을 사용 중인지 확인

- **Docker에서 MySQL이 완전히 기동되었는지 확인**

  ```bash
  docker logs ai_restaurant_db
  ```

  초기화 완료 로그 이후 접속해야 연결됨

---

### 📦 `mysql_data`는 어디에 저장될까?

- `docker-compose.yml`에서 지정된 `mysql_data:/var/lib/mysql` 설정은 다음을 의미:
  - `mysql_data`는 **Docker 볼륨 이름**입니다.
  - `/var/lib/mysql`은 MySQL 컨테이너 내부의 데이터 저장 위치입니다.
- 실제 데이터는 **Docker가 내부적으로 관리하는 볼륨 공간**에 보관됩니다.

#### 🔍 현재 Docker 볼륨 확인

```bash
docker volume ls
```

예시 출력:

```
DRIVER    VOLUME NAME
local     ai-restaurant_mysql_data
local     ai_rest_mysql_data
...
```

#### 🔍 볼륨 경로 확인

```bash
docker volume inspect ai-restaurant_mysql_data
```

예시 결과:

```json
"Mountpoint": "/var/lib/docker/volumes/ai-restaurant_mysql_data/_data"
```

> 이 경로는 Linux에서만 직접 접근 가능하며, Windows는 WSL2 또는 Docker Desktop 내부에서 관리됩니다.

---

### ✅ 정리

- `localhost:3305`로 DBeaver에서 Docker MySQL 접속 가능
- 연결이 안 되면 컨테이너 상태, 포트 충돌, 비밀번호 등 점검 필요
- 데이터는 `mysql_data`라는 이름의 Docker 볼륨에 안전하게 저장됩니다

