from guias.models import guias
from rest_framework import viewsets, permissions
from .serializers import RegistroSerializer

# guias Viewset 
class guiasViewset(viewsets.ModelViewSet):
    queryset = guias.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegistroSerializer

