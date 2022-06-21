from musculation.models import Exercice
from rest_framework import viewsets
from .serializers import ExerciceSerializer
# from django.contrib.auth.models import User
 
 
# ViewSets define the view behavior.
"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""
    
    
class ExerciceViewSet(viewsets.ModelViewSet):
    queryset = Exercice.objects.all()
    serializer_class = ExerciceSerializer