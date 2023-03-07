from django.db import models

# Create your models here.
class Ledger(models.Model):
    spent_money = models.IntegerField()
    memo = models.TextField(blank=True)
    day = models.DateTimeField()

    def __str__(self):
        return self.title   