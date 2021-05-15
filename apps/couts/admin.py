from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.
admin.site.register(models.CoutFibreOptique)
admin.site.register(models.CoutAdsl)
admin.site.register(models.CoutGoInternetMobile)
admin.site.register(models.LicenceFai)
admin.site.register(models.LicenceGsm)