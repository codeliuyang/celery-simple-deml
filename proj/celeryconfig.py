"""
celery config
see https://docs.celeryproject.org/en/latest/userguide/configuration.html
"""
broker_url = "redis://localhost:6379/0"
timezone = "Asia/Shanghai"
enable_utc = True
include = ['proj.tasks']    # 引入包含任务的module