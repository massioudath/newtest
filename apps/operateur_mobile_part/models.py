from django.db import models

# Create your models here.
class OperateurMobilePart(models.Model):
    operateur = models.CharField(max_length=50, null=True)
    part = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operateur_mobile_part'

