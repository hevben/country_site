from django.contrib import admin

from .models import Country
from .models import Form
from .models import Continent


admin.site.register(Country)
admin.site.register(Form)
admin.site.register(Continent)

# Register your models here.
