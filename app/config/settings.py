"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

base_settings = [
    'components/apps_middleware.py',
    'components/authorization.py',
    'components/common.py',
    'components/database.py',
    'components/hosts.py',
    # 'components/debug_logging.py',
    'components/templates.py',
]

include(*base_settings)