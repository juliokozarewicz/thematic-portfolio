from django.contrib import admin
from .models import Work


@admin.register(Work)

class Post_admin(admin.ModelAdmin):

    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}