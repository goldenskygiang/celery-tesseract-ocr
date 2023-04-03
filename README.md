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