from musculation.models import Exercice
from rest_framework import serializers
# from django.contrib.auth.models import User


# Serializers define the API representation.
"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    model = User
    fields = ['url', 'username', 'email', 'is_staff', 'is_superuser', 'last_login']_
"""
     
     
class ExerciceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercice
        fields = ['name', 'weight', 'seconds_rest_time', 'rehearsals', 'series']
