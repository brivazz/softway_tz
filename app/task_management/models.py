from django.utils.translation import gettext_lazy as _
from django.db import models


class Task(models.Model):

    class TaskType(models.TextChoices):
        DONE = 'done', _('Done'),
        NOT_DONE = 'not done', _('Not done')

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    status = models.CharField(
        _('status'), max_length=20, choices=TaskType.choices, default=TaskType.NOT_DONE)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    class Meta:
        db_table = 'tasks'
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.title
