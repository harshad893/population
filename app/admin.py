from django.contrib import admin

# Register your models here.
from app.models import *
class WebpageCustomize(admin.ModelAdmin):
    list_display=('topic_name','name','url')
    list_display_links=['name']
    list_editable=['url']
    list_per_page=3
    search_fields=['name']
    list_filter=['topic_name']

admin.site.register(Topic)
admin.site.register(Webpage,WebpageCustomize)
admin.site.register(Access_Records)