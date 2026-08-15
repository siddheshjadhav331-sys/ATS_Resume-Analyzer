from django.urls import path
from . import views

urlpatterns = [

    path(
        'upload-resume/',
        views.upload_resume,
        name='upload_resume'
    ),
    
    path(
    'analysis/',
    views.analysis_view,
    name='analysis'
),

]