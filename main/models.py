from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField(max_length=5000)     
    author=models.CharField(max_length=300)
    image=models.URLField(default=None, null=True)
    linktosite=models.URLField(default=None, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def search_category(cls,search):
        searches = cls.objects.filter(name__icontains = search)
        return searches


class Review(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.TextField(max_length=1500)
    rating=models.FloatField(default=0)
    def __str__(self):
        return self.user.username