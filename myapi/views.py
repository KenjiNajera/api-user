

# Create your views here.

from rest_framework import  viewsets

from .serializers import EmpleadoSerializer, UserSerializer
from .models import Empleado, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset= Empleado.objects.all()
    serializer_class=EmpleadoSerializer