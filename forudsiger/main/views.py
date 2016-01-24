from django.shortcuts import render, redirect
from django.http import HttpResponse

#forms
from .forms import *

#models
from main.models import *

#user stuff
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

#error messages to users
from django.contrib import messages

#time
from django.utils import timezone


#views
def index(request):
    return render(request, 'main/index.html', {'form': LoginForm()})

#events
def events(request):
    return render(request, 'main/begivenheder.html', {"events": Event.objects.all()})

#single event
def event(request, begivenhed_id):
    #if it doesn't exist, give an error
    try:
        event = Event.objects.get(id = begivenhed_id)
    except:
        return redirect("error_page")

    #if was a prediction
    if request.method == "POST":
        #get predicted value
        predicted_value = request.POST['prediction']

        #make prediction
        event = models.ForeignKey(Event)

        #who made it
        user = models.ForeignKey(User)

        #what the prediction is
        prediction = models.CharField(max_length=10)

        #which date the prediction was made
        date = models.DateTimeField("prediction made")
        prediction = Prediction(
            event = Event.objects.get(id = begivenhed_id),
            user = request.user,
            prediction = predicted_value,
            date = timezone.now())
        
        #save prediction
        prediction.save()

        #reload page, with success message
        messages.info(request, "Succes! Du har lavet en forudsigelse. Lav nogle flere!")
        return redirect("event", begivenhed_id = begivenhed_id)

    #user predictions on this event
    user_predictions = Prediction.objects.filter(user = request.user, event = Event.objects.get(id = begivenhed_id))

    #if it does, show it
    return render(request, "main/begivenhed.html", {"event": event, "user_predictions": user_predictions})

#predictions
def predictions(request):
    return render(request, 'main/forudsigelser.html', {"predictions": Prediction.objects.all()})

#make_prediction
def make_prediction(request):
    return HttpResponse("make a prediction")

#leaderboard
def leaderboard(request):
    return HttpResponse("leaderboard")

#login page
def login_page(request):
    #user already logged in?
    if request.user.is_authenticated():
        #was it a logout?
        if request.method == "POST":
            if request.POST["logout"] == "True":
                logout(request)
                return redirect("index")

        #is user a staff member?
        if request.user.is_staff:
            #show link to admin panel too
            return render(request, 'main/login.html', {"logged_in": True, "staff": True})

        #show user profile/logout
        return render(request, 'main/login.html', {"logged_in": True})

    #user not logged in
    if not request.user.is_authenticated():

        #was it a login attempt?
        if request.method == "POST":

            #fetch login data
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:

                #is user active? then login the user
                if user.is_active:
                    login(request, user)

                    #redirect to batches page or to where the user wanted to go
                    # pdb.set_trace()
                    # if "next" in request.GET:
                    #     return redirect(request.GET["next"])
                    return redirect("index")
                #user is inactive, don't log in user
                else:
                    #redirect to error page
                    messages.error(request, "Din bruger er blevet deaktiveret! Øv!")
                    return redirect("login_page")

            else:
                #return to the login page and show an error message
                messages.error(request, 'Brugernavnet eller koden var desværre forkert. Prøv igen. :)')
                return redirect("login_page")

        #if not a login attempt, show default site
        return render(request, 'main/login.html', {'form': LoginForm()})

def error_page(request):
    return HttpResponse("Der er opstået en fejl. Ups!")
