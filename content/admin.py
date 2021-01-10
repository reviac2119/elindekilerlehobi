from django.contrib import admin
from content.models import Content


# Register your models here.
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'publishing_date', 'link']
    list_display_links = ['category', 'publishing_date']
    list_filter = ['publishing_date']
    list_editable = ['title', 'link']
    search_fields = ['title', 'ingredients', 'category']

    class Meta:
        model = Content


admin.site.register(Content, ContentAdmin)
