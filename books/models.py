from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ADMIN = 'admin'
    AUTHENTICATED_USER = 'authenticated_user'
    GUEST = 'guest'

    USER_ROLES = (
        (ADMIN, 'Admin'),
        (AUTHENTICATED_USER, 'Authenticated User'),
        (GUEST, 'Guest'),
    )

    role = models.CharField(max_length=20, choices=USER_ROLES, default=AUTHENTICATED_USER)

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=200)

    def __str__(self):
        return self.title
