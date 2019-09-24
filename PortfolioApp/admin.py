from django.contrib import admin

# Register your models here.
from PortfolioApp.models import HeroArea, MyDetail, Education, Experience, Contact, Mywork, TechnicalSkill, WorkSumarry

admin.site.register(HeroArea)
admin.site.register(MyDetail)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(TechnicalSkill)
admin.site.register(WorkSumarry)


class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact

    list_display = ['name', 'sub', 'email', 'message']


admin.site.register(Contact, ContactAdmin)


class MyworkAdmin(admin.ModelAdmin):
    class Meta:
        model = Mywork

    list_display = ['project_title', 'project_image', 'project_github_link','project_detail']


admin.site.register(Mywork, MyworkAdmin)