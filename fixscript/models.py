from django.db import models


class Fixscript(models.Model):
    app = models.CharField(max_length=100)
    identifier = models.SmallIntegerField()

    def __str__(self):
        return "{self.app}-{self.identifier}"

    class Meta:
        unique_together = ['app', 'identifier']
