FROM python:3.8-slim

RUN pip install --upgrade pip

RUN useradd -m myuser

USER myapp

WORKDIR /home/myapp

COPY --chown=myuser:myuser . /home/myapp

RUN pip install -r requirements.txt

CMD ["python", "-m", "flask run", "--port=8000", "--module=myapp"]
