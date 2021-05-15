from django.db import models

# Create your models here.
class Opendnsv4Stat(models.Model):
    nbre_odr = models.IntegerField(blank=True, null=True)
    save_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opendnsv4_stat'
