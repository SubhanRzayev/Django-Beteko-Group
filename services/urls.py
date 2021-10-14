from django.urls import path
from .views import ServiceDetailView, ServiceView,ProjectView,ProjectDetailView
app_name = 'services'

urlpatterns = [
    path("service/", ServiceView.as_view(), name="service"),
    path("service-detail/<int:pk>/", ServiceDetailView.as_view(), name="service_detail"),
    path("projects/", ProjectView.as_view(), name="projects"),
    path("projects-detail/<int:pk>/", ProjectDetailView.as_view(), name="projects_detail")
    
]


