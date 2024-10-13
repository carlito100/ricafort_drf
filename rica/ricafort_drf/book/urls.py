from django.urls import path
from .views import AuthorViewSet, CategoryViewSet, BookViewSet

urlpatterns = [
    path('author/<int:pk>/', AuthorViewSet.as_view({'patch': 'update', 'delete': 'destroy'}), name='author-detail'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'patch': 'update', 'delete': 'destroy'}), name='category-detail'),
    path('book/<int:pk>/', BookViewSet.as_view({'patch': 'update', 'delete': 'destroy'}), name='book-detail'),
]
