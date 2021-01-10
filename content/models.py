from django.db import models
from django.urls import reverse
# Create your models here.


class Content(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=30)
    ingredients = models.TextField()
    explanation = models.TextField()
    publishing_date = models.DateField()
    link = models.CharField(max_length=50, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})

    class Meta:
        ordering = ['category', 'title']


class Comment(models.Model):
    content = models.ForeignKey('content.Content', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='İsim')
    textComment = models.TextField(verbose_name='Yorum')
    created_date = models.DateTimeField(auto_now_add=True)