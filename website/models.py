from django.db import models
from services.models import UserAccount


# Create your models here.

class Acceille(models.Model):

    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/Acceille")
    description = models.TextField()
    date = models.DateField()
    comentaire = models.IntegerField()
    vue = models.IntegerField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:

        verbose_name = 'Acceille'
        verbose_name_plural = 'Acceilles'

    def __str__(self):
       return self.nom

class Fashion(models.Model):

    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/fashion")
    description = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:

        verbose_name = 'Fashion'
        verbose_name_plural = 'Fashions'

    def __str__(self):
       return self.nom
       
class Gallerie(models.Model):

    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/gallerie")
    description = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:

        verbose_name = 'Gallerie'
        verbose_name_plural = 'Galleries'

    def __str__(self):
       return self.nom

class Contact(models.Model):
    message = models.TextField()
    nom = models.CharField(max_length = 255)
    mail = models.EmailField()
    sujet = models.CharField(max_length = 255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="contact"
        verbose_name_plural = "contacts"

    def __str__(self):
        return self.nom 

class NewsLetter(models.Model):
    mail = models.EmailField() 
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="newsLetter"
        verbose_name_plural = "newsletters"

    def __str__(self):
        return str(self.mail)          