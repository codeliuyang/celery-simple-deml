1. 启动beat server
celery -A proj beat

2. 启动celery任务
celery -A proj worker -l info