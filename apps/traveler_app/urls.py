from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^success$', views.index, name = "dashboard"),
    url(r'^add$', views.add, name = "add_trip"),
    url(r'^create$', views.create, name = "create_trip"),
    url(r'^trip_location$', views.trip_location, name = "trip_location"),
]
