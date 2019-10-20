from .base import *

DATABASES = {
    'default': {
        'ENGINE': get_env_variable('PRO_DB_ENGINE'),
        'NAME': get_env_variable('PRO_DB_NAME'),
        'USER': get_env_variable('PRO_DB_USER'),
        'PASSWORD': get_env_variable('PRO_DB_PASSWORD'),
        'POST': '3306',
        'OPTION': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}
