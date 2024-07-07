from django.contrib import admin

from core.movies.models import Movie


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ["title", "description", "actors"]
    list_display = ["id", "title", "description"]
    search_fields = ["id", "title"]
