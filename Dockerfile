FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip \
  && pip install -r requirements.txt

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
