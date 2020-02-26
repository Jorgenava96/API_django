from rest_framework import routers
from .api import guiasViewset

routers = routers.DefaultRouter()
routers.register('api/guias')