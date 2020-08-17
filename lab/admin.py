from django.contrib import admin
from .models import Labrepair


@admin.register(Labrepair)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'lab', 'system', 'problem', 'lab_status')

