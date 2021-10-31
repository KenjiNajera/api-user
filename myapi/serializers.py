from django.db.models import fields
from rest_framework import serializers
from .models import Empleado, User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'first_name','last_name','avatar')

class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Empleado
        fields=('id','nombre','apellido','correo','fechaIngreso')