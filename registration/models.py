from django.db import models
from django.contrib.auth.models import AbstractUser


class FactionUser(AbstractUser):
    IMPERIAL = 'Imp'
    REPUBLIC = 'Pub'
    FACTION_CHOICES = (
        (IMPERIAL, 'Imperial'),
        (REPUBLIC, 'Republic'),
    )
    faction = models.CharField(
        max_length=3,
        choices=FACTION_CHOICES,
        default=IMPERIAL
    )

    def __unicode__(self):
        return self.username
