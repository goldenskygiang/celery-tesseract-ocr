from app.celery import celeryapp

from PIL import Image

import pytesseract
import json

@celeryapp.task
def extract_ocr(img_path: str):
    with Image.open(img_path) as img:
        txt = pytesseract.image_to_string(img_path)
        res = {
            'img_path': img_path,
            'text': txt
        }
        return res