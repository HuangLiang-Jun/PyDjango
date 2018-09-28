from django.db import models

# Create your models here.

# db_table == table name 自定義table名稱
class FX(models.Model):
    currency_cn = models.CharField(max_length=20, primary_key=True, default=None)
    currency_en = models.CharField(max_length=20, default=None)
    cash_buying = models.CharField(max_length=20, default=None)
    cash_selling = models.CharField(max_length=20, default=None)
    spot_buying = models.CharField(max_length=20, default=None)
    spot_selling = models.CharField(max_length=20, default=None)
    update_date = models.CharField(max_length=20, default=None)
    
    class Meta:
        db_table = 'FX'#table name
    

class Bank(models.Model):
    bank_name = models.CharField(max_length = 20, default = None)
    bank_code = models.CharField(max_length = 20, default = None)
    class Meta:
        db_table = 'bank'

class Currency(models.Model):
    currency_cn = models.CharField(max_length=20, default=None)
    currency_en = models.CharField(max_length=20, default=None, unique=True)
    
    class Meta:
        db_table = 'currency'

class ExchangeRate(models.Model):
    
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    cash_buying = models.CharField(max_length=20, default=None)
    cash_selling = models.CharField(max_length=20, default=None)
    spot_buying = models.CharField(max_length=20, default=None)
    spot_selling = models.CharField(max_length=20, default=None)
    
    class Meta:
        db_table = 'exchange_rate'

class ExchangeRateUpdateTime(models.Model):
    
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    update_date = models.CharField(max_length=20, default=None)
    class Meta:
        db_table = 'exchange_rate_update_time'
    