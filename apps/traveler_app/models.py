from __future__ import unicode_literals
from ..loginreg_app.models import User
from django.db import models

# Create your models here.
class TravelerManager(models.Manager):
    def create_trip(self, form_data,user):
        return self.create(
            destination = form_data['destination'],
            description = form_data['description'],
            travel_start = form_data['travel_start'],
            travel_end = form_data['travel_end'],
            user = user,
        )

    def travel_validate(self, form_data):

        errors = []

        if len(form_data['destination']) == 0:
            errors.append("You have to pick a place to go.")

        if len(form_data['description']) == 0:
            errors.append("Put what you want to do.")
        #Travel Start
        if not form_data['travel_start']:
            errors.append("When do you want to leave?")
        #travel future date validation
        else:
            if datetime.strptime(form_data['travel_start'], "%Y-%m-%d") < datetime.today():
                errors.append("Your departure must be in the future.")
            #travel end
            if not form_data['travel_end']:
                errors.append("Unfortunately you have to come home, so pick a date!")
            else:
                if datetime.strptime(form_data['travel_end'], "%Y-%m-%d") < datetime.strptime(form_data['travel_start'], "%Y-%m-%d"):
                    errors.append("You have to leave before you can return.")

        return errors





class Traveler(models.Model):
    destination = models.CharField(max_length = 255)
    description = models.TextField()
    travel_start = models.DateField()
    travel_end = models.DateField()
    buddy = models.ManyToManyField(User, related_name ="buddy")
    planner = models.ForeignKey(User, related_name = "planner")
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)

    objects = TravelerManager()

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.id, self.destination, self.description, self.travel_start, self.travel_end, self.buddy, self.planner)
