from django.urls import path
from .views import Home, delete, GRAPH, remove

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('delete', delete, name='delete'),
    path('graph', GRAPH.as_view(), name='graph'),
    path('remove', remove, name='remove'),
]