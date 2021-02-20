from celery import Task
from .celery import app
from crontasks.onemintask import onemintask
from crontasks.twomintask import twomintask
from .db import get_db_info


db_session, db_map_classes = get_db_info()


class BaseTask(Task):
    """An abstract Task, the aim:
       (1) ensures that the connection the the database is closed on task completion"""
    abstract = True

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        db_session.remove()


@app.task(base=BaseTask)
def add(x, y):
    onemintask()
    Transformer = db_map_classes.transformer
    query = db_session.query(Transformer).first()
    print(query)
    print(str(x) + str(y) + '=' + str(x + y))


@app.task(base=BaseTask)
def abc(x, y):
    twomintask()
    User = db_map_classes.user
    query = db_session.query(User).first()
    print(query)
    print(str(x) + str(y) + '=' + str(x + y))