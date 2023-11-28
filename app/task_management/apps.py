from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TaskManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_management'
    verbose_name = _('task_management')
