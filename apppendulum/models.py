from django.db import models
import math

# Create your models here.

class Pendulum(models.Model):
    l1 = models.FloatField(default=150)
    l2 = models.FloatField(default=120)
    theta1 = models.FloatField(default=math.pi / 2)
    theta2 = models.FloatField(default=math.pi / 2)
    m1 = models.FloatField(default=0.1)
    m2 = models.FloatField(default=0.1)
    color = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.color + " -  " + str(self.id)

class Graph(models.Model):
    axis_l = models.CharField(max_length=100)
    axis_b = models.CharField(max_length=100)

    def __str__(self):
        return self.axis_l + " <-> " + self.axis_b