from django.db import models


class Entry(models.Model):
    """A digital signature in the guest book."""
    datetime = models.DateTimeField(False, True)
    ip = models.IPAddressField()
    nameFirst = models.CharField(max_length=32)
    nameLast = models.CharField(max_length=32)
    comment = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.comment + ' -' + nameFirst + ' ' + nameLast