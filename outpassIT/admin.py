from django.contrib import admin
from .models import IT

@admin.register(IT)
class ITAdmin(admin.ModelAdmin):
    list_display = ('id', 'it_name', 'it_rollnumber', 'it_year', 'it_branch', 'it_reason', 'it_start_date',
                    'it_end_date', 'it_applydate', 'it_permission')

