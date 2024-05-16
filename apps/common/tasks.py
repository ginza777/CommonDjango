from celery import shared_task, Celery

app = Celery('task', broker='redis://localhost:6379/0')


@shared_task()
def custom_task():
    pass
