bind = '0.0.0.0:5000'
workers = 1

errorlog = '-'
loglevel = 'debug'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
spew = False


# errorlog = '/var/log/gunicorn/error.log'
# accesslog = '/var/log/gunicorn/access.log'