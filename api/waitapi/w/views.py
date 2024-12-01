from rest_framework import viewsets
from rest_framework.response import Response
from .models import Workout, Exercise
from .serializers import WorkoutSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
