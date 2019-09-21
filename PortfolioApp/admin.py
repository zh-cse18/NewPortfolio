from django.contrib import admin

# Register your models here.
from PortfolioApp.models import HeroArea, MyDetail, Education, Experience

admin.site.register(HeroArea)
admin.site.register(MyDetail)
admin.site.register(Education)
admin.site.register(Experience)
