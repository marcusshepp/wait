from rest_framework import viewsets
from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
