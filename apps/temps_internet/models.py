from django.db import models

# Create your models here.
class TempsInternet(models.Model):
    #time remplacer temps_moyens
    temps_moyens_internet = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'temps_internet'
