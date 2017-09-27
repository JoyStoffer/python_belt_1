from django.shortcuts import render
from ..loginreg_app.models import User
from .models import Traveler
# Create your views here.
def index(request):

    return render(request, 'traveler_app/index.html')

def current_user(request):
    return User.objects.get(id = request.session['user_id'])

def add(request):
    return render(request, 'traveler_app/add.html')

def trip_location(request):
    return render(request, 'traveler_app/destination.html')

def success(request):
    if 'user_id' in request.session:
        context = {
            'user':current_user(request)
        }
        return render(request, 'traveler_app/index.html', context)

    return render(reverse('landing'))

def flash_errors(errors, request):
    for error in errors:
        messages.error(request, error)


def create(request):
    if request.method =="POST":
        #validate data
        errors = Traveler.objects.travel_validate(request.POST)
        print "********************errors on create travel*************"
        #check if errors don't exist
        if not errors:
            #create_trip
            trip = Traveler.objects.create_trip(request.POST)

            user = User.objects.create_user(request.POST)

            return redirect(reverse('destination', kwargs={'id':traveler.id}))

        flash_errors(errors,request)
    return redirect(reverse('create_trip'))
