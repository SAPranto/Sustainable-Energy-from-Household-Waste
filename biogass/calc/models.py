from django.db import models

# Create your models here.
class predict(models.Model):
    
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Gas = models.FloatField()

    class Meta:
        managed = False
        db_table = 'predict'