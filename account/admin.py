from django.contrib import admin
from .models import Profile, CallbackRequest


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'ID_number', 'date_of_birth', 'photo']


@admin.register(CallbackRequest)
class CallbackRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'id_number', 'phone', 'called']
