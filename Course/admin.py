# from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ('title', 'content',)


# class PostAdmin(SummernoteModelAdmin):
#     list_display = ('title', 'slug',)
#     search_fields = ('title', 'content',)
#     summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
