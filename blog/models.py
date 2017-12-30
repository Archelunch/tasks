from django.conf import settings
from django.db import models
from django.utils.timezone import now
# Create your models here.
class Tag(models.Model):
    tagname = models.CharField(max_length=30, default="[Undefinded]")

    def __str__(self):
        return self.tagname

class Post(models.Model):
    title = models.CharField(max_length=130)
    date = models.DateTimeField(default=now, verbose_name='Дата публикации')
    content = models.TextField(max_length=5000)
    tags = models.ManyToManyField(Tag, related_name="tag_post", verbose_name='Теги')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/p%i/" % self.id



class Comment(models.Model):
    comment = models.CharField(max_length=500)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)
    com = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        primary_key=False,
        default=None,
        related_name='comments')

    def __str__(self):
        return self.comment
