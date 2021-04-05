import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookStore.settings')

app = Celery('BookStore')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'data_synchronization': {
        'task': 'store.tasks.data_synchronization',
        'schedule': crontab(minute=0, hour=0)
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')  # noqa: T001