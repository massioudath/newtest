from django.db import models

# Create your models here.
class TopSite(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'top_site'