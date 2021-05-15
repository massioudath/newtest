from django.db import models

# Create your models here.
class ReseauSocial(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)


class NumberUser(models.Model):
    abonnes = models.IntegerField()
    reseaux = models.ForeignKey('ReseauSocial', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)