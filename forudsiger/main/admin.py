from django.contrib import admin

from .models import Prediction, Event


## More colons in admin panel

class EventAdmin(admin.ModelAdmin):
    list_display = ('description', 'pub_date', "last_date", "end_date", "prediction_type", "creator", "id")
    search_fields = ['description']

class PredictionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "event", "prediction", "date")

#register models in admin
admin.site.register(Event, EventAdmin)
admin.site.register(Prediction, PredictionAdmin)
