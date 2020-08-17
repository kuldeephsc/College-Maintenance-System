from django.contrib import admin
from .models import Hostel

# Register your models here.
@admin.register(Hostel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','student_name', 'userid', 'hostel', 'floor', 'room', 'appliances', 'status')
# Register your models here.
