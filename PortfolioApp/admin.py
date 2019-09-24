from django.contrib import admin

# Register your models here.
from PortfolioApp.models import HeroArea, MyDetail, Education, Experience, Contact, Mywork, TechnicalSkill, WorkSumarry, \
    MyActivity

admin.site.register(HeroArea)
admin.site.register(MyDetail)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(WorkSumarry)


class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact
    list_display = ['name', 'sub', 'email', 'message']


class MyworkAdmin(admin.ModelAdmin):
    class Meta:
        model = Mywork
    list_display = ['project_title', 'project_image', 'project_github_link','project_detail']


class TechnicalAdmin(admin.ModelAdmin):
    list_display = ['topic_name', 'topic_completed']


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['icon_name', 'sector_name']


admin.site.register(MyActivity, ActivityAdmin)
admin.site.register(Mywork, MyworkAdmin)
admin.site.register(TechnicalSkill, TechnicalAdmin)
admin.site.register(Contact, ContactAdmin)
