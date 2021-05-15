from django.db import models

# Create your models here.
class CoutCoupure(models.Model):
    cout_coupure_internet= models.FloatField(blank=True, null=True)
    cout_coupure_facebook = models.FloatField(blank=True, null=True)
    cout_coupure_twitter= models.FloatField(blank=True, null=True)
    cout_coupure_instagram = models.FloatField(blank=True, null=True)
    cout_coupure_whatsapp = models.FloatField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cout_coupure'