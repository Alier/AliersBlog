from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

    def getDateOnly(self):
        return self.pub_date.strftime('%b %e，%Y')

    def summary(self):
        return self.body[:100]
