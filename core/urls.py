from django.urls import path
from core.views import *


app_name = 'core'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about")

]

