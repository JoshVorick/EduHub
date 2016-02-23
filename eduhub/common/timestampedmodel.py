from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super(TimestampedModel, self).save(*args, **kwargs)
