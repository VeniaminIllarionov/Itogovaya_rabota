from django.contrib import admin

from services.models import Service, Record


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('id',)
    search_fields = ('name', 'description',)


@admin.register(Record)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'doctor')
    list_filter = ('id', 'created_at')
    search_fields = ('user', 'created_at',)


