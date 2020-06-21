from django.contrib import admin
from core.models import Records

from .models import Records
from .models import Imagesz

# Register your models here.

admin.site.register(Records)
admin.site.register(Imagesz)