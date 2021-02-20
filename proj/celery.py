from celery import Celery
from celery.schedules import crontab

app = Celery()
app.config_from_object("proj.celeryconfig")


app.conf.beat_schedule = {
    'one-min-task': {
        'task': 'proj.tasks.add',
        'schedule': crontab(minute='*'),
        'args': (16, 16),
    },
    'two-min-task': {
        'task': 'proj.tasks.abc',
        'schedule': crontab(minute='*/2'),
        'args': (12, 12),
    },
}

