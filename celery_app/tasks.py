# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import shared_task
from datetime import datetime
from email_send import sendMail, listen_nginx


@shared_task(track_started=True)
def listen_ngx_celery():
    try:
        res = listen_nginx()
        if res.status_code != 200:
            print('not 200', datetime.now(), res)
            error_info = u'Nginx服务器似乎出了问题，\r\n状态码{0}，\r\n{1}，\r\n请立即查看。'.format(
                res.status_code, res.json
            )
            sendMail(error_info)

        else:
            print("It's ok", datetime.now())
    except Exception as e:
        print('Exception!!', datetime.now(), e)
        error_info = u'Nginx服务器似乎出了问题，\r\n{0}，\r\n请立即查看'.format(e)
        sendMail(error_info)
