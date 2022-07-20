from django.contrib import admin

# Register your models here.
from .models import Contact


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_on', 'updated_on')
