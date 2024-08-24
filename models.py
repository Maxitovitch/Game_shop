
from django.db import models
import random
import string

from django.db import models
from django.contrib.auth.models import AbstractUser, User




class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.ForeignKey(Genre, related_name='games', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order', null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_code()
        super().save(*args, **kwargs)

    def generate_code(self):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        while Order.objects.filter(code=code).exists():
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return code

from django.db import models
from django.contrib.auth.models import User

class SupportTicket(models.Model):
    subject = models.CharField(max_length=100)  # Тема запроса
    email = models.EmailField()  # Email пользователя
    message = models.TextField()  # Сообщение
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.subject



