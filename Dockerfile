# 베이스 이미지로 Python 3.9 사용
FROM python:3.11-slim

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 업데이트 및 필수 패키지 설치
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \    
    build-essential \
    pkg-config \
    nginx \
    curl \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
    apt-get clean
    


# 필요한 Python 패키지 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# nginx 설정 복사
COPY nginx.conf /etc/nginx/conf.d/default.conf


# sql proxy 설치
RUN curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.13.0/cloud-sql-proxy.linux.amd64 && \
    chmod +x cloud-sql-proxy

# 애플리케이션 소스 복사
COPY . /app/
COPY django_project_key.json /app/credentials.json


RUN python manage.py collectstatic --noinput  

# 포트 노출
EXPOSE 8080

# Django 서버 실행
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
# Run Cloud SQL Proxy
CMD ./cloud-sql-proxy --credentials-file credentials.json --address 0.0.0.0 --port 3306 my-project2-441007:us-central1:oksusu-database & \
gunicorn mydocker.wsgi:application --bind 127.0.0.1:8000 & \
nginx -g "daemon off;"



# Copy Cloud SQL Proxy credentials

# 프로젝트 ID
# my-project2-441007
# docker run -d -v D:\docker_project(django)\mydocker\django_project_key.json:/path/to/service-account-key.json -p 127.0.0.1:3308:3306 gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.13.0 --address 0.0.0.0 --port 3306 --credentials-file /path/to/service-account-key.json my-project2-441007:us-central1:oksusu-database

# 도커이미지 생성명령어
# docker buildx build --platform linux/amd64 -t gcr.io/my-project2-441007/docker_project .

# 도커이미지 실행명령어
#docker run -d -p 8080:8080 --name docker_project gcr.io/my-project2-441007/docker_project:20250101
#docker run -d -p 8080:8080 --name django_project oksusu2020/django_project:20250116