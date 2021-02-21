from django.contrib import admin
from .models import (MacroCycle, MesoCycle, WorkoutWeeks, WorkoutDays, WorkoutExercises, Exercises, MuscleGroups)


admin.site.register(MacroCycle)
admin.site.register(MesoCycle)
admin.site.register(WorkoutWeeks)
admin.site.register(WorkoutDays)
admin.site.register(WorkoutExercises)
admin.site.register(Exercises)
admin.site.register(MuscleGroups)