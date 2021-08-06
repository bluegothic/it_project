from django.contrib import admin
from rango.models import Topic, UserProfile, Comment


# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    pass
    # list_display = ('author_id', 'topic_id', 'context', 'date')


admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile)
