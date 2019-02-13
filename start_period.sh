cd /root/www/period/
source kkwork/bin/activate
celery -B -A celery_app worker -l info