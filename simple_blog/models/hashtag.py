from django.db import models


class HashTag(models.Model):
    name = models.CharField(max_length=255, blank=False)
    key = models.TextField(max_length=255, blank=False, unique=True)
    parent_hash_tag = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'hash_tags'

    def __str__(self) -> str:
        return self.key
