from django.db import models

# Create your models here.

# class name == table name
class FX(models.Model):
    currency_cn = models.CharField(max_length=20, primary_key=True)
    currency_en = models.CharField(max_length=20)
    cash_buying = models.CharField(max_length=20)
    cash_selling = models.CharField(max_length=20)
    spot_buying = models.CharField(max_length=20)
    spot_selling = models.CharField(max_length=20)
    update_date = models.CharField(max_length=20)
    class Meta:
        managed = True
        db_table = 'FX'#table name


    