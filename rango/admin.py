from django.contrib import admin
from rango.models import Category, Page, UserProfile, Comment


# Register your models here.
class PageAdmin(admin.ModelAdmin):
  list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields={'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)


class commentAdmin(admin.ModelAdmin):
  list_display = ('author_id', 'topic_id', 'context', 'date')
admin.site.register(Comment, commentAdmin)