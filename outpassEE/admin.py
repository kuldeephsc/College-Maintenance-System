from .models import EE
from django.contrib import admin


@admin.register(EE)
class EEAdmin(admin.ModelAdmin):
    list_display = ('id', 'ee_name', 'ee_rollnumber', 'ee_year', 'ee_branch', 'ee_reason', 'ee_start_date',
                    'ee_end_date', 'ee_applydate', 'ee_permission')




# Register your models here.
