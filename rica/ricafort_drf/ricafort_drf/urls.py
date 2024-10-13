# book/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book  # Adjust the import based on your model structure
from .serializers import BookSerializer  # Make sure this is correctly set up

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()  # Get all books
        serializer = BookSerializer(books, many=True)  # Serialize the books
        return Response(serializer.data)  # Return the serialized data

