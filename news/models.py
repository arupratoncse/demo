from django.db import models


class News(models.Model):
    """News Model"""
    class Meta:
        db_table = 'news'
        ordering = ['pk']

    author = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    description = models.TextField()
    url = models.CharField(max_length=1000)
    urlToImage = models.CharField(max_length=1000)
    publishedAt = models.DateTimeField()
