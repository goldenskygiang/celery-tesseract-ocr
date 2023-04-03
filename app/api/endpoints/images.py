from app.api.deps import get_db
from app.services.ocr import tasks as ocr
from app.models.image import TaskResult

from fastapi import APIRouter, Depends, UploadFile, HTTPException
from sqlalchemy.orm import Session
from PIL import Image

import os
import uuid

router = APIRouter()

@router.get('/{id}')
def get_ocr(id: str, db: Session = Depends(get_db)):
    obj = db.query(TaskResult).filter(TaskResult.task_id == id).first()
    print(obj)
    return obj.result

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