from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_at')

    readonly_fields = ('text', 'author', 'created_at')

    search_fields = ('text', 'author__username')

    list_filter = ('author',)

# Register your models here.
