import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtu6e.settings')

app = Celery('youtu6e')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'check_submit_status': {
        'task': 'celery_app.tasks.update_submit_status',
        'schedule': 10.0,
    },
    'send_solution': {
        'task': 'celery_app.tasks.send_submit_to_cats',
        'schedule': 6.0,
    }
}