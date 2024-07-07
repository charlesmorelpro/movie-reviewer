from django.contrib import admin

from core.reviews.models import Review


# Register your models here.
@admin.register(Review)
class ActorAdmin(admin.ModelAdmin):
    fields = ["grade", "movie"]
    list_display = ["id", "grade", "movie"]
