FROM python:3.12

SHELL ["/bin/bash", "-c"]

# set project variables
FOLDER="shop"
USERNAME="dooky"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash $USERNAME && chmod 777 /opt /run

WORKDIR /$FOLDER

RUN mkdir /$FOLDER/static && mkdir /$FOLDER/media && chown -R $USERNAME:$USERNAME /$FOLDER && chmod 755 /$FOLDER

COPY --chown=$USERNAME:$USERNAME . .

RUN pip3 install -r requirements.txt

USER $USERNAME

CMD ["gunicorn","-b","0.0.0.0:8001","app.wsgi"]
