# Celery OCR

A web application to extract text from images, using Celery as task queue.

## Prerequisite

Install `tesseract-ocr` for OCR functionalities.

```
sudo apt install tesseract-ocr
```

## API routes

`GET /images/:id`: get image and its text using the ID.

`POST /images`: post an image, return its ID for further lookup.

## How to run

Open a terminal session then type
```
celery -A app worker --loglevel=INFO
```

Open another session and type

```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Or, just type `docker compose up` since I have updated Docker scripts.