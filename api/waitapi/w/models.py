from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Workout on {self.date_created}"


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Sett(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='sets')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # In kg or lbs
    reps = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.exercise.name} - {self.reps} reps @ {self.weight}"


class Cardio(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='cardio_sessions')
    cardio_type = models.CharField(max_length=100)  # e.g., running, cycling, etc.
    duration = models.DurationField()  # Store duration as a timedelta
    distance = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # In km or miles

    def __str__(self):
        return f"{self.cardio_type} for {self.duration}"



