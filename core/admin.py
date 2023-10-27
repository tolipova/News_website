from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.utils.html import mark_safe
# Register your models here. 
class NewsAdmin(admin.ModelAdmin):
    list_display = ('category')

admin.site.register(Posts)
admin.site.register(Category)

