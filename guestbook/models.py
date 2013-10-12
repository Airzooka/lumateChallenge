from django.core import validators
from django.db import models


class Entry(models.Model):
    """A digital signature in the guest book."""
    datetime = models.DateTimeField(False, True)
    ip = models.IPAddressField()
    namefirst = models.CharField(
        max_length=32,
        validators=[
            validators.RegexValidator(
                r'^[A-Za-z0-9 \'-]{1,32}$',
                'First name is invalid.',
                'Invalid First Name'
                )
            ]
        )
    namelast = models.CharField(
        max_length=32,
        validators=[
            validators.RegexValidator(
                r'^[A-Za-z0-9 \'-]{1,32}$',
                'Last name is invalid.',
                'Invalid Last Name'
                )
            ]
        )
    comment = models.TextField(
        blank=True,
        validators=[
            validators.RegexValidator(
                r'^[A-Za-z0-9 \'"!?.]{0,256}$'
                'Comment is invalid. Keep it simple!',
                'Invalid Comment'
                )
            ]
        )
    
    def __unicode__(self):
        return self.comment + ' -' + nameFirst + ' ' + nameLast