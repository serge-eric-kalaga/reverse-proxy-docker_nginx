FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

# RUN apt-get update && apt-get install -y nginx

# EXPOSE 5001

CMD [ "python", "app.py"]