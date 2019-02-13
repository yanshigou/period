# -*- coding: utf-8 -*-
from celery import Celery


app = Celery("listen_ngx")
app.config_from_object('celery_app.celeryconf')  # 加载配置模块
