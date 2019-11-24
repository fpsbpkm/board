from django.db import models


# Create your models here.
class Contents(models.Model):
    main_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='image', blank=True, null=True)


class ImageSize(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
