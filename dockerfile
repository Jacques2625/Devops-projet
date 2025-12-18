FROM python:3.13

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/code

EXPOSE 80

ENTRYPOINT ["uvicorn", "code.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

