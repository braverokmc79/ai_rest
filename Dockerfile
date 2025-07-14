FROM python:3.12.2-slim-bullseye

WORKDIR /usr/src/ai_rest_backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# mysqlclient 빌드에 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    netcat \
    && rm -rf /var/lib/apt/lists/*

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev python3-dev cargo


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/ai_rest_backend/entrypoint.sh
RUN chmod +x /usr/src/ai_rest_backend/entrypoint.sh

COPY . .

ENTRYPOINT [ "/usr/src/ai_rest_backend/entrypoint.sh" ]
