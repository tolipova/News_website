from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.utils.html import mark_safe
# Register your models here. 
class NewsAdmin(admin.ModelAdmin):
    list_display = ('category')

class PostsAdmin(admin.ModelAdmin):
    list_display = ('category','title','date','get_html_photo',)

    def get_html_photo(self,object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width="50">')
        return None
    get_html_photo.short_description = 'Surat'

admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Featured)
admin.site.register(MainSilder)
admin.site.register(StartSlider)


