"""Admin for django_admin_shell."""

from django.contrib import admin

from .models import SavedSnippets


class SavedSnippetsAdmin(admin.ModelAdmin):
    """Admin for SavedSnippets."""

    list_display = ('name', 'code')
    search_fields = ('name', 'code')

admin.site.register(SavedSnippets, SavedSnippetsAdmin)
