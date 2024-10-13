from django.contrib import admin
from .models import Book, Author, Category

# Define an admin class for the Author model
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_date', 'gender')  # Fields to display in the admin list view
    search_fields = ('name',)  # Fields that can be searched

# Define an admin class for the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Fields to display in the admin list view

# Define an admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'isbn', 'author', 'category', 'created_at')  # Fields to display
    search_fields = ('name', 'isbn')  # Fields that can be searched
    list_filter = ('author', 'category')  # Add filters for author and category

# Register the models with the admin site
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
