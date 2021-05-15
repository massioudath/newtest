from django.db import models
# Create your models here.
class Penetration(models.Model):
    internet_fixe = models.FloatField(blank=True, null=True)
    internet_mobile = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'penetration'
