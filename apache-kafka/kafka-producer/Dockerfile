FROM python:3.9

LABEL maintainer="Minamohammadi"

WORKDIR /app

COPY . /app
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

CMD ["python3", "app.py"]
