from django.core import validators
from django.db import models

class Entry(models.Model):
    """A digital signature in the guest book."""
    datetime = models.DateTimeField(auto_now_add=True)
    ip = models.IPAddressField()
    namefirst = models.CharField(
        max_length=32,
        validators=[
            validators.RegexValidator(
                regex=r'^[A-Za-z0-9 \'-]+$',
                message='First name is invalid.',
                code='Invalid First Name'
                )
            ],
        error_messages = {
            'blank': 'First name must be provided.',
            'max_length': 'Last name must be 32 characters or less.'
            }
        )
    namelast = models.CharField(
        max_length=32,
        validators=[
            validators.RegexValidator(
                regex=r'^[A-Za-z0-9 \'-]+$',
                message='Last name is invalid.',
                code='Invalid Last Name'
                )
            ],
        error_messages = {
            'blank': 'Last name must be provided.',
            'max_length': 'Last name must be 32 characters or less.'
            }
        )
    comment = models.CharField(
        blank=True,
        max_length=200,
        error_messages = {
            'max_length': 'Comment must be 200 characters or less.'
            }
        )
    
    def __unicode__(self):
        return self.comment + ' -' + nameFirst + ' ' + nameLast