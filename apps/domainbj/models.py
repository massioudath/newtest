
from django.db import models

# Create your models here.

class Domain(models.Model):
    total_domain = models.IntegerField(blank=True, null=True)
    actifs_domain = models.IntegerField(blank=True, null=True)
    expired_domain = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'domain'
