from django.contrib import admin
from .models import Messfeedback

@admin.register(Messfeedback)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'meal', 'rating', 'review', 'feedback_date')


