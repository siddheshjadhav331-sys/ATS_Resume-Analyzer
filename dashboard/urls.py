from django.urls import path
from . import views

urlpatterns = [

    path(
        'candidate-dashboard/',
        views.candidate_dashboard,
        name='candidate_dashboard'
    ),

    path(
        'recruiter-dashboard/',
        views.recruiter_dashboard,
        name='recruiter_dashboard'
    ),

    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),
]