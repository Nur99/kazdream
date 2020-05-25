from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .serializers import CarSerializer
from .models import Car
from utils.decorators import response_wrapper


@method_decorator(response_wrapper(), name='dispatch')
class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
