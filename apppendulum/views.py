from django.shortcuts import render, redirect
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

class Home(APIView):
    serializer_class = PendulumSerializer
  
    def get(self, request):
        pendulum = [ {"l1": pendulum.l1, "l2": pendulum.l2, "theta1": pendulum.theta1, "theta2": pendulum.theta2, "m1": pendulum.m1, "m2": pendulum.m2, "color":pendulum.color, "id": pendulum.id} 
        for pendulum in Pendulum.objects.all()]
        return Response(pendulum)
  
    def post(self, request):
        serializer = PendulumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  redirect("https://aritraspendulum.netlify.app/")

class GRAPH(APIView):
    serializer_class = GraphSerializer
  
    def get(self, request):
        graph = [ {'axis_l': graph.axis_l, 'axis_b': graph.axis_b} 
        for graph in Graph.objects.all()]
        return Response(graph)
  
    def post(self, request):
        serializer = GraphSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  redirect("https://aritraspendulum.netlify.app/")

@ensure_csrf_cookie
def delete(request):
    if request.method == "POST":
        id = request.POST['delete']
        pendulum  = Pendulum.objects.filter(pk=id)
        pendulum.delete()

    return redirect("https://aritraspendulum.netlify.app/")

@ensure_csrf_cookie
def remove(request):
    if request.method == "POST":
        axis_l = request.POST['graph'].split(':')[0]
        axis_b = request.POST['graph'].split(':')[1]
        graph = Graph.objects.filter(axis_l=axis_l, axis_b=axis_b)
        graph.delete()

    return redirect("https://aritraspendulum.netlify.app/")