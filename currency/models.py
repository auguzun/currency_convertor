from django.db import models


class Currency(models.Model):
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)
    type = models.CharField(verbose_name="Currency type", unique=True, max_length=50)
    exchange_rate = models.DecimalField(verbose_name="Exchange rate to base currency",
                                        max_digits=10, decimal_places=3, null=True)

    def __str__(self):
        return str(self.type)

    class Meta(object):
        db_table= 'currency'


