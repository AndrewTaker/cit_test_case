from django.db import models


class City(models.Model):
    name = models.CharField(
        verbose_name='Название города',
        max_length=250
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name='Широта',
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name='Долгота',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'latitude', 'longitude'], name='unique geodata'
            )
        ]
        verbose_name = 'город'
        verbose_name_plural = 'города'
        default_related_name = 'cities'
        ordering = ['name']
        get_latest_by = 'datetime'

    def __str__(self):
        return self.name
