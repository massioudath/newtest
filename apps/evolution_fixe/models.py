from django.db import models

# Create your models here.
class EvolutionFixe(models.Model):
    technologie = models.CharField(max_length=255, blank=True, null=True)
    evolution = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evolution_fixe'
