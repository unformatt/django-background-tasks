# -*- coding: utf-8 -*-
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'TEST':  # This will force django to create a real sqlite database on
                 # the disk, instead of creating it in memory.
                 # We need this to test the async behavior.
            {
                'NAME': 'test_db',
            },
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'background_task',
]

SECRET_KEY = 'foo'

USE_TZ = True
BACKGROUND_TASK_RUN_ASYNC = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': u'[%(levelname)s] %(name)s:%(funcName)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
    },
    'loggers': {
        'background_task': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
