from django.contrib import admin
from .models import App


class AppAdmin(admin.ModelAdmin):
    list = (
        'title',
        'author',
        'date',
        'last_edit',
        'article',
    )


admin.site.register(App, AppAdmin)