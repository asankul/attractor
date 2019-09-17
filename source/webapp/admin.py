from django.contrib import admin
from webapp.models import Article


class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title', 'description', 'status', 'date']
    list_filter = ['title', 'description']
    search_fields = ['title', 'description', 'status']
    fields = ['title', 'description', 'status', 'date']


admin.site.register(Article, ArticleAdmin)
