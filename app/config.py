#DATABASE_URL = 'sqlite:///./celery_ocr.db'
DATABASE_URL = "postgresql://postgres:postgres@localhost/celery-ocr"

CELERY_BACKEND = f'db+{DATABASE_URL}'
CELERY_BROKER = 'redis://default:redispw@localhost:32768'