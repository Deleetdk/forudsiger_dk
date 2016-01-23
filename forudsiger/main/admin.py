from django.contrib import admin

from .models import Prediction, Event

admin.site.register(Event)
admin.site.register(Prediction)
