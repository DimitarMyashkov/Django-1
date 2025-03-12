from django.db import models

class PageCount(models.Model):
    count = models.IntegerField(default = 0)
