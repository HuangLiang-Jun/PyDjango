from django.db import models

# Create your models here.

# class name == table name
class FX(models.Model):
    currency_cn = models.CharField(max_length=20, primary_key=True, default=None.)
    currency_en = models.CharField(max_length=20, default=None.)
    cash_buying = models.CharField(max_length=20, default=None.)
    cash_selling = models.CharField(max_length=20, default=None.)
    spot_buying = models.CharField(max_length=20, default=None.)
    spot_selling = models.CharField(max_length=20, default=None.)
    update_date = models.CharField(max_length=20, default=None.)
    class Meta:
        managed = True
        db_table = 'FX'#table name


    