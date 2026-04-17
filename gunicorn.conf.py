bind = '0.0.0.0:8080'
workers = 2
threads = 2
timeout = 120
wsgi_app = 'config.wsgi:application'
accesslog = '-'
errorlog = '-'
loglevel = 'debug'
