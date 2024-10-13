from django.contrib import admin
from django.urls import include, pathfrom django.urls import path
from . import views

urlpatterns = [
    path('api/books/', views.BookList.as_view(), name='book-list'),
    # Add other paths here
]


urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line to include admin URLs
    path('book/', include('book.urls')),
]
