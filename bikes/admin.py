from django.contrib import admin
from django.utils.html import format_html
from .models import Bike

# Register your models here.
class BikeEdit(admin.ModelAdmin):
    def tumpnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px" alt="photo">'.format(object.bike_photo.url))

    tumpnail.short_description = 'Photo'
    list_display = ('id','tumpnail','bike_title','city','year','is_featured')
    list_display_links = ('id','tumpnail','bike_title',)
    list_editable = ('is_featured',)
    search_fields = ('id','bike_title','city','year','is_featured')
    list_filter = ('bike_title','city','year','is_featured')
admin.site.register(Bike, BikeEdit)