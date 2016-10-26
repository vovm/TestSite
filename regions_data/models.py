from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region)
    name = models.CharField(max_length=150)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class Parse(models.Model):
    file_name = models.FileField(upload_to='csv')

    def __str__(self):
        return "File № {}".format(self.id)
