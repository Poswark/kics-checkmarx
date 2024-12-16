FROM python:3.12.2-alpine3.19 as builder

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN apk update --no-cache  && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app



RUN addgroup -S appuser && adduser -S appuser -G appuser
USER appuser


EXPOSE 5050
HEALTHCHECK CMD curl --fail http://localhost:5050 || exit 1 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5050"]
