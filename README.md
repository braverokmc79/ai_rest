# Django 웹 프로그래밍 강좌 정리

본 강좌는 Django를 활용한 웹 프로그래밍을 배우기 위한 기초 강좌로, 프로젝트 생성부터 Git 사용법, 데이터베이스 모델링, Django View 및 Form, 테스트 작성, 정적 파일 관리, Admin 커스터마이징 등을 다룹니다.


### 파이썬·장고 웹개발 | 코담 - 코드에 세상을 담다

[![코담 소개 이미지](https://codam.kr/assets/images/og-image.jpg)](https://codam.kr/)

---


# 🚀 AI REST Backend 프로젝트 README

## 📦 Docker Compose 실행 방법

1. **Docker 이미지 빌드 및 컨테이너 실행**

   ```bash
   docker compose up --build
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
