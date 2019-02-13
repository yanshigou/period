# -*- coding: utf-8 -*-
from celery.schedules import crontab


BROKER_URL = "redis://localhost:6379/1"
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = False

# 导入指定的任务模块
CELERY_IMPORTS = ('celery_app.tasks',)


# 下面是定时任务的设置
CELERYBEAT_SCHEDULE = {
    # 定时任务:　每1分钟，执行任务(listen_ngx_celery)
    'Listen_ngx': {
        'task': 'celery_app.tasks.listen_ngx_celery',
        'schedule': crontab(minute='*/2'),
        "args": ()
    },
}
