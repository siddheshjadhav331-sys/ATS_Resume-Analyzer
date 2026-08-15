from django.urls import path
from . import views

urlpatterns = [

    path(
        'create-job/',
        views.create_job,
        name='create_job'
    ),

    path(
        'jobs/',
        views.jobs_list,
        name='jobs_list'
    ),

    path(
        'candidate-jobs/',
        views.candidate_jobs,
        name='candidate_jobs'
    ),

    path(
        'apply/<int:job_id>/',
        views.apply_job,
        name='apply_job'
    ),

    path(
        'applicants/',
        views.applicants,
        name='applicants'
    ),

    path(
        'rankings/',
        views.rankings,
        name='rankings'
    ), 

    path(
    'profile/',
    views.profile,
    name='profile'
    ),

]