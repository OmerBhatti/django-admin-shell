"""Models for django_admin_shell."""

from django.db import models


class SavedSnippets(models.Model):
    """Models to contain saved snipets."""

    name = models.CharField(max_length=32)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        """Meta class for SavedSnippets."""

        verbose_name = "Saved Snippet"
        verbose_name_plural = "Saved Snippets"

    def __str__(self):
        """Return name of saved snippet."""
        return self.name
