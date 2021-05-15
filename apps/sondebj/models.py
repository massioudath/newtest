from django.db import models

# Create your models here.
class Sonde(models.Model):
    total = models.IntegerField(blank=True, null=True)
    abandonned = models.IntegerField(blank=True, null=True)
    connected = models.IntegerField(blank=True, null=True)
    disconnected = models.IntegerField(blank=True, null=True)
    never_connected = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sonde'
