from django.db import models

# Create your models here.
class RepartitionTechnologie(models.Model):
    technologie = models.CharField(max_length=225, blank=True, null=True)
    repartition = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repartition_technologie'
