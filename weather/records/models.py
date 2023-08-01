from django.db import models


class Record(models.Model):
    city = models.ForeignKey(
        verbose_name='Город',
        to='locations.city',
        on_delete=models.CASCADE,
    )
    datetime = models.DateTimeField(verbose_name='Дата и время')
    c_value = models.IntegerField(verbose_name='Температура в цельсиях')

    @property
    def f_value(self):
        return (self.c_value * 9 // 5) + 32

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['city', 'datetime'],
                name='unique city/datetime value',
            )
        ]
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        default_related_name = 'records'
        ordering = ['-city']
        get_latest_by = 'datetime'

    def __str__(self):
        return f"{self.city.name} || {self.datetime}"
