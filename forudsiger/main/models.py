from django.db import models
from django.contrib.auth.models import User

#models
from main.models import *

class Event(models.Model):
    #description of event
    description = models.TextField()

    #longer description of event
    description_long = models.TextField()

    #truth conditions
    truth_conditions = models.TextField()

    #start date
    pub_date = models.DateTimeField('date published')

    #last prediction
    last_date = models.DateTimeField("last prediction date")

    #ending date
    end_date = models.DateTimeField("ending date")

    #the kinds of predictions for the event
    choices = [
    ["d", "dichotomous"],
    ["v", "value"]]
    prediction_type = models.CharField(max_length=10, choices = choices)

    #creator of the event
    creator = models.ForeignKey(User) #default to the admin user (site)

    #conditional event?
    conditional = models.BooleanField(default = False)

    #number of predictions about this event
    def number_predictions(self):
        x = len(Prediction.objects.filter(event = self))
        if x == None:
            return 0
        return x
    
    #unique users with predictions
    def unique_users(self):
        event_predictions = (Prediction.objects.filter(event = self))
        event_users = [prediction.user for prediction in event_predictions]
        unique_users = len(set(event_users))
        if unique_users == None:
            return 0
        return unique_users
    
    #number of predictions by the user
    def number_user_predictions(self, user):
        user_predictions = len(Prediction.objects.filter(event = self, user = user))
        if user_predictions == None:
            return 0
        return user_predictions


class Prediction(models.Model):
    #which event
    event = models.ForeignKey(Event)

    #who made it
    user = models.ForeignKey(User)

    #what the prediction is
    prediction = models.CharField(max_length=10)

    #which date the prediction was made
    date = models.DateTimeField("prediction made")

