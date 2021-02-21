from django.db import models
from django.contrib.auth.models import User

class MacroCycle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, blank=False)
    description = models.TextField(blank=True)
    duration = models.IntegerField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MesoCycle(models.Model):
    macro_id = models.ForeignKey(MacroCycle, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, blank=False)
    description = models.TextField(blank=True)
    duration = models.IntegerField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WorkoutWeeks(models.Model):
    meso_id = models.ForeignKey(MesoCycle, on_delete=models.CASCADE)
    week_nr = models.IntegerField()
    name = models.CharField(max_length=80)
    description = models.TextField()
    number = models.IntegerField()

    def __str__(self):
        return self.name


class WorkoutDays(models.Model):
    week_id = models.ForeignKey(WorkoutWeeks, on_delete=models.CASCADE)
    day = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return f'week_id={self.week_id}, day={self.day}'


class MuscleGroups(models.Model):
    name = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return self.name

class Exercises(models.Model):
    name = models.CharField(max_length=80, blank=False)
    muscle_group_id = models.ForeignKey(MuscleGroups, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class WorkoutExercises(models.Model):
    day = models.ForeignKey(WorkoutDays, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, blank=True)
    description = models.TextField()
    exercise_id = models.ForeignKey(Exercises, on_delete=models.CASCADE)

    def __str__(self):
        return self.name















