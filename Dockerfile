FROM python:3.8-slim

RUN pip install --upgrade pip

RUN adduser -D myuser

USER myapp

WORKDIR /home/myapp

COPY --chown=myuser:myuser ./* .

RUN pip install -r requirements.txt

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
