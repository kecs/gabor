FROM divio/base:1.1-py3.10-slim-bullseye-dev
RUN apt-get update
WORKDIR /gabor
COPY . /gabor
RUN pip install -r requirements.pip
RUN python manage.py collectstatic --noinput
EXPOSE 80
CMD gunicorn --bind=0.0.0.0:80 --forwarded-allow-ips="*" gabor.wsgi:application