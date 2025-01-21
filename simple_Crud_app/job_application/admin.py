from django.contrib import admin
from job_application.models import Form

class FormAdmin(admin.ModelAdmin):
    list_dispaly = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter =("first_name", "last_name", "email")
    ordering = ("first_name", )
    readonly_fields = ("first_name", "last_name", "email")

admin.site.register(Form, FormAdmin)
# Register your models here.
