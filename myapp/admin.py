from django.contrib import admin
from myapp.models import *

# Register your models here.

class WebpageAdminView(admin.ModelAdmin):
    list_display = ('top_name',"name","url") #what to display to admin
    list_per_page = 5  # no of records per page
    list_editable = ('name','url') # it makes the field editable
    search_fields = ('name',)  # it creates a search fields
    list_filter = ('top_name',) #  it filters the columns by given name. eg: 'top_name' it must be primary key
    


class Access_DetailsAdminView(admin.ModelAdmin):
    list_display = ('name','date')
    list_per_page = 5

admin.site.register(Topic)
admin.site.register(Webpage, WebpageAdminView)
admin.site.register(Access_Details, Access_DetailsAdminView)
    