from django.db import models

# Create your models here.
class RoutingsecStat(models.Model):
    nbre_prefixeip_tested = models.IntegerField(blank=True, null=True)
    nbre_ro_true = models.IntegerField(blank=True, null=True)
    nbre_rpki_true = models.IntegerField(blank=True, null=True)
    save_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routingsec_stat'
