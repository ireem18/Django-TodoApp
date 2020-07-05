from django.contrib import admin

from user.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['type','clicked','note', 'create_at','complated_time', 'status']
    list_filter = ['status']




admin.site.register(Todo,TodoAdmin)
