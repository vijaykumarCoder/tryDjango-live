from django.contrib import admin
#import models from modesl file
from . import models

# Register your models here.
admin.site.register(models.products)
admin.site.register(models.Order)

