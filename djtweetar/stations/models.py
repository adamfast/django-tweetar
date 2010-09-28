from django.db import models

class Station(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    auto_post = models.BooleanField()

    def __unicode__(self):
        return self.code
