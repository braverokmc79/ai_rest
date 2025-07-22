
import os
from pathlib import Path
from dotenv import load_dotenv



BASE_DIR = Path(__file__).resolve().parent.parent


# 1. 기본적으로 .env 로드 (여기서 ENV 값만 읽는다)
load_dotenv(dotenv_path=BASE_DIR / ".env")
ENV = os.environ.get("ENV", "dev")

# 2. 환경별 .env 파일 분기 로드
if ENV == "prod":
    load_dotenv(dotenv_path=BASE_DIR / ".env.prod", override=True)
else:
    load_dotenv(dotenv_path=BASE_DIR / ".env.dev", override=True)


# ✅ Github Actions & 테스트 환경에서는 SQLite 사용
if os.environ.get('GITHUB_ACTIONS') == 'true' or os.environ.get("TEST"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # 🌱 개발/운영 환경 MySQL
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ.get("DB_NAME"),
            "USER": os.environ.get("DB_USER"),
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "HOST": os.environ.get("DB_HOST"),
            "PORT": os.environ.get("DB_PORT"),
            "OPTIONS": {
                "charset": "utf8mb4",
                "init_command": "SET NAMES utf8mb4",
            }
        }
    }
    
# Use Amazon S3 for storage for uploaded media files if not debugging
if os.environ.get("S3_BUCKET"):
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "bucket_name": os.environ.get("S3_BUCKET"),
                "region_name": os.environ.get("S3_REGION", "ap-northeast-2"),
                "custom_domain": os.environ.get("S3_CUSTOM_DOMAIN"),
                "location": "media",
                "default_acl": "public-read",
                "querystring_auth": False,
            },
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "bucket_name": os.environ.get("S3_BUCKET"),
                "region_name": os.environ.get("S3_REGION", "ap-northeast-2"),
                "custom_domain": os.environ.get("S3_CUSTOM_DOMAIN"),
                "location": "static",
                "default_acl": "public-read",
                "querystring_auth": False,
            },
        },
    }    
    
    
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# 강력한 시크릿 키 생성 (예시)
#python -c "import secrets; print(secrets.token_urlsafe(64))"
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "jXhxB_DiqtanAczI_whLI1_Xzs8GdwVkyuiI_5KE4ApUCQPH6fa2Bg7QvEOyLOWwryWzW60_lruVQvAfs_Db8Q"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"


ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "restaurant",    
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "proj.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'templates'],      
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "proj.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }




# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"





# HSTS 설정 (1년)
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# # HTTPS 강제 리다이렉트
# SECURE_SSL_REDIRECT = True
# # 쿠키를 HTTPS 전용으로만
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

#SECURE_HSTS_SECONDS = 31536000  # 1년 권장
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


print("DB_HOST:", os.environ.get("DB_HOST"))