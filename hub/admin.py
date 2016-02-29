from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from hub.models import Topic, Resource, Provider, TopicSet, Tag
from easy_select2 import select2_modelform


class TopicAdmin(DjangoMpttAdmin):
    pass


class CoveredTopicsInlineAdmin(admin.TabularInline):
    model = Resource.covered_topics.through
    form = select2_modelform(Resource.covered_topics.through, attrs={'width': '250px'})


class RequiredTopicsInlineAdmin(admin.TabularInline):
    model = Resource.required_topics.through
    form = select2_modelform(Resource.required_topics.through, attrs={'width': '250px'})


class TagInlineAdmin(admin.TabularInline):
    model = Resource.tags.through
    form = select2_modelform(Resource.tags.through, attrs={'width': '250px'})


class ResourceAdmin(admin.ModelAdmin):
    inlines = (CoveredTopicsInlineAdmin, RequiredTopicsInlineAdmin, TagInlineAdmin, )
    form = select2_modelform(Resource, attrs={'width': '250px'})


class ProviderAdmin(admin.ModelAdmin):
    pass


class TopicSetAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Resource, ResourceAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(TopicSet, TopicSetAdmin)
admin.site.register(Tag, TagAdmin)
