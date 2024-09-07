enable environment source Email/bin/activate

To start Server use 
- python3 manage.py runserver
- celery -A emailworker worker
- redis-server
- celery -A emailworker flower
