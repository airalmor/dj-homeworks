from django.db import models



class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, db_column='sensor', on_delete=models.CASCADE, related_name='measurements')
    temperature = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)