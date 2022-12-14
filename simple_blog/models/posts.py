from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=True)
    user = models.ForeignKey(
        'simple_blog.User', on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    hashtags = models.ManyToManyField(
        'simple_blog.HashTag', related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'

    def __str__(self) -> str:
        return self.content
