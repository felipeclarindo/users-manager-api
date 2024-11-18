from django.contrib.auth.hashers import make_password, is_password_usable
from django.core.exceptions import ValidationError
from django.utils import timezone
from validate_docbr import CPF
from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True)
    login = models.CharField(max_length=70, unique=True)
    senha = models.CharField(max_length=150)  
    email = models.EmailField(max_length=125, unique=True)

    def save(self, *args, **kwargs):
        self.cpf = self.cpf.strip().replace(".", "").replace("-", "")
        if not CPF().validate(self.cpf):
            raise ValidationError("Invalid CPF")

        if self.senha and not self.senha.startswith(('pbkdf2_sha256$', 'bcrypt')):
            self.senha = make_password(self.senha)

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.login