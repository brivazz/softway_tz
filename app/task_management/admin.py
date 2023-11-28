from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'created_at')
    list_filter = ('title', 'status')
    search_fields = ('title', 'status')
    save_on_top = True
    save_as = True


admin.site.site_title = 'Управление задачами'
admin.site.site_header = 'Управление задачами'
