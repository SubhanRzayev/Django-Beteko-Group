from django.urls import path
from core.views import *


app_name = 'core'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("careers", CareersView.as_view(), name="careers"),
    path("careers-detail/<int:pk>/", CareersDetailView.as_view(),name="careers_detail"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about"),
    path("approach/", ApproachView.as_view(), name="approach"),
    

]

