from django.contrib import admin

# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display= ('name', 'email', 'message', 'created_on', 'updated_on')

admin.site.register(Contact, ContactAdmin)