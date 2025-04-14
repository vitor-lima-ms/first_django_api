from django.contrib import admin
from courses.models import Course, Rating

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at', 'updated_at', 'active')
    search_fields = ('title', 'url')
    list_filter = ('active',)
    list_per_page = 10

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'email', 'rating', 'created_at', 'updated_at', 'active')
    search_fields = ('course', 'name', 'email')
    list_filter = ('rating',)
    list_per_page = 10