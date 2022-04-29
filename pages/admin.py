from django.contrib import admin
from .models import Team
from django.utils.html import format_html
class TeamAdmin(admin.ModelAdmin):
    def tumpnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px" alt="photo">'.format(object.photo.url))

    tumpnail.short_description = 'Photo'
    list_display = ('id','tumpnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('id','tumpnail','first_name',)
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)
admin.site.register(Team, TeamAdmin)

