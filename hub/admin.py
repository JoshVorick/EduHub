from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from hub.models import Topic, EduSource, EduProvider, TopicSet
from easy_select2 import select2_modelform


class TopicAdmin(DjangoMpttAdmin):
    pass


class CoveredTopicsInlineAdmin(admin.TabularInline):
    model = EduSource.covered_topics.through
    form = select2_modelform(EduSource.covered_topics.through, attrs={'width': '250px'})


class RequiredTopicsInlineAdmin(admin.TabularInline):
    model = EduSource.required_topics.through
    form = select2_modelform(EduSource.required_topics.through, attrs={'width': '250px'})


class EduSourceAdmin(admin.ModelAdmin):
    inlines = (CoveredTopicsInlineAdmin, RequiredTopicsInlineAdmin, )
    form = select2_modelform(EduSource, attrs={'width': '250px'})


class EduProviderAdmin(admin.ModelAdmin):
    pass


class TopicSetAdmin(admin.ModelAdmin):
    pass

admin.site.register(EduSource, EduSourceAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(EduProvider, EduProviderAdmin)
admin.site.register(TopicSet, TopicSetAdmin)
