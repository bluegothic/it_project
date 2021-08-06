from django.contrib import admin
from rango.models import Topic, Page, UserProfile, Comment


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Topic, TopicAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)


class commentAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'topic_id', 'context', 'date')


admin.site.register(Comment, commentAdmin)
