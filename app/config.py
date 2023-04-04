import os

DATABASE_URL = 'sqlite:///./celery_ocr.db'
#DATABASE_URL = "postgresql://postgres:postgres@localhost/celery-ocr"

CELERY_BACKEND = f'db+{DATABASE_URL}'
CELERY_BROKER = os.environ.get('REDIS_URL', 'redis://default:redispw@localhost:32772')