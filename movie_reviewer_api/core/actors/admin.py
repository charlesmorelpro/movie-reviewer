from django.contrib import admin

from core.actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name']
    list_display = ['id', 'first_name', 'last_name']
    search_fields = ['id', 'first_name']