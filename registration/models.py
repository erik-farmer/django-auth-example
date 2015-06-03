from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    IMPERIAL = 'Imp'
    REPUBLIC = 'Pub'
    FACTION_CHOICES = (
        (IMPERIAL, 'Imperial'),
        (REPUBLIC, 'Republic'),
    )
    user = models.OneToOneField(User)
    faction = models.CharField(
        max_length=3,
        choices=FACTION_CHOICES,
        default=IMPERIAL
    )

    def __unicode__(self):
        return self.user.username
