from django.db import models

# Create your models here.
class DebitRegion(models.Model):
    index = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    median_download = models.FloatField(blank=True, null=True)
    median_upload = models.FloatField(blank=True, null=True)
    download = models.IntegerField(blank=True, null=True)
    upload = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debit_region'


