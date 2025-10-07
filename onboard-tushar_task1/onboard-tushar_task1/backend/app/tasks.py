from celery import Celery
import os
celery = Celery('tasks', broker=os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0'))

@celery.task
def send_email_task(recipient_id: str, html: str, subject: str):
    # Replace with actual DB lookup and provider call
    print("Celery: send_email_task", recipient_id, subject)
    return True
