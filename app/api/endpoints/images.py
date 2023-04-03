from app.api.deps import get_db
from app.services.ocr import tasks as ocr
from app.celery import celeryapp

from fastapi import APIRouter, Depends, UploadFile, HTTPException
from sqlalchemy.orm import Session
from PIL import Image
from celery.result import AsyncResult

import os
import uuid

router = APIRouter()

@router.get('/{id}')
def get_ocr(id: str):
    obj = ocr.extract_ocr.AsyncResult(id)
    if obj.ready():
        return obj.get()
    else:
        raise HTTPException(404, 'not found or processed yet')

@router.post('/')
def upload_img(file: UploadFile):
    # upload the image then process it with a service
    try:
        img = Image.open(file.file)
        img.verify()

        # copy the image to tmp dir
        os.makedirs('img_tmp', exist_ok=True)
        
        img = Image.open(file.file)
        filename = f'{uuid.uuid4()}.{str.lower(img.format)}'
        filepath = f'img_tmp/{filename}'

        filepath = os.path.abspath(filepath)
        img.save(filepath)

        task = ocr.extract_ocr.delay(filepath)
        return {
            'id': task.id
        }
    except Exception as e:
        print(e)
        raise HTTPException(400, e.args)