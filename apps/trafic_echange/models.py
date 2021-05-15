from django.db import models

# Create your models here.
class TraficEchange(models.Model):
    url_trafic = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'trafic_echange'