from django.contrib import admin
from .models import ME


@admin.register(ME)
class MEAdmin(admin.ModelAdmin):
    list_display = ('id', 'me_name', 'me_rollnumber', 'me_year', 'me_branch', 'me_reason', 'me_start_date',
                    'me_end_date', 'me_applydate', 'me_permission')


from django.contrib import admin

# Register your models here.
