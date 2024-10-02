"""Admin for django_admin_shell."""

from django.contrib import admin

from .models import SavedSnippet


class SavedSnippetAdmin(admin.ModelAdmin):
    """Admin for SavedSnippet."""

    list_display = ('id', 'name', 'created_at', 'code')
    search_fields = ('name', 'code')


admin.site.register(SavedSnippet, SavedSnippetAdmin)
