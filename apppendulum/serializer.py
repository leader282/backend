from rest_framework import serializers
from . models import *
  
class PendulumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendulum
        fields = ['l1', 'l2', 'theta1', 'theta2', 'm1', 'm2', 'color']

class GraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graph
        fields = ['axis_l', 'axis_b']