from django.contrib import admin

from doctors.models import Doctor
from services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('id',)
    search_fields = ('name', 'description',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic', 'work_experience')
    list_filter = ('id',)
    search_fields = ('name', 'patronymic',)
