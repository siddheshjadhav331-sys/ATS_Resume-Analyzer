from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from resumes.models import Resume

@login_required
def candidate_dashboard(request):

    resumes = Resume.objects.filter(
        candidate=request.user
    )

    latest_resume = resumes.last()

    score = 0

    if latest_resume:
        score = latest_resume.ats_score

    return render(
        request,
        'candidate/dashboard.html',
        {
            'resumes': resumes,
            'score': score
        }
    )

@login_required
def recruiter_dashboard(request):

    return render(
        request,
        'recruiter/dashboard.html'
    )


@login_required
def admin_dashboard(request):

    return render(
        request,
        'adminpanel/dashboard.html'
    )