from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line to include admin URLs
    path('book/', include('book.urls')),
]
