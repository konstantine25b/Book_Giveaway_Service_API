from rest_framework import viewsets, permissions,status
from .models import *
from .serializers import *
from rest_framework.response import Response
from .permissions import IsAdmin ,Is_Authenticated_User

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status = status.HTTP_201_CREATED , headers = headers)
        else:
            return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
        
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [Is_Authenticated_User]

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [Is_Authenticated_User]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

