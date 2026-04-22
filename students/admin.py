from django.contrib import admin
from .models import Student, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "email", "enrollment_date"]
    search_fields = ["first_name", "last_name", "email"]
    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "isbn", "student"]
    search_fields = ["title", "author", "isbn"]
    list_filter = ["student"]
