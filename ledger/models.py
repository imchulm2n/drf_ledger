from django.db import models

# Create your models here.

class Ledger(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    spent_money = models.IntegerField(default=0)
    earned_money = models.IntegerField(default=0)
    memo = models.CharField(max_length=100)
    balance = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.memo
    