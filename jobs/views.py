
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import (
    login_required
)

from .models import (
    Job,
    Application
)

from .forms import JobForm

from resumes.models import Resume


@login_required
def create_job(request):

    if request.method == 'POST':

        form = JobForm(
            request.POST
        )

        if form.is_valid():

            job = form.save(
                commit=False
            )

            job.recruiter = request.user

            job.save()

            return redirect(
                'jobs_list'
            )

    else:

        form = JobForm()

    return render(
        request,
        'recruiter/create_job.html',
        {
            'form': form
        }
    )


@login_required
def jobs_list(request):

    jobs = Job.objects.filter(
        recruiter=request.user
    )

    return render(
        request,
        'recruiter/jobs_list.html',
        {
            'jobs': jobs
        }
    )


@login_required
def candidate_jobs(request):

    jobs = Job.objects.all()

    applied_jobs = Application.objects.filter(
        candidate=request.user
    ).values_list(
        'job_id',
        flat=True
    )

    return render(
        request,
        'candidate/jobs.html',
        {
            'jobs': jobs,
            'applied_jobs': applied_jobs
        }
    )


@login_required
def apply_job(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    already_applied = Application.objects.filter(
        candidate=request.user,
        job=job
    ).exists()

    if not already_applied:

        resume = Resume.objects.filter(
            candidate=request.user
        ).last()

        ats_score = 0

        if resume:

            ats_score = resume.ats_score

        Application.objects.create(
            candidate=request.user,
            job=job,
            ats_score=ats_score
        )

    return redirect(
        'candidate_jobs'
    )


@login_required
def applicants(request):

    applications = Application.objects.filter(
        job__recruiter=request.user
    )

    return render(
        request,
        'recruiter/applicants.html',
        {
            'applications': applications
        }
    )


@login_required
def rankings(request):

    applications = Application.objects.filter(
        job__recruiter=request.user
    ).order_by(
        '-ats_score'
    )

    return render(
        request,
        'recruiter/rankings.html',
        {
            'applications': applications
        }
    )

@login_required
def profile(request):

    applications = Application.objects.filter(
        candidate=request.user
    )

    resumes = Resume.objects.filter(
        candidate=request.user
    )

    latest_resume = resumes.last()

    score = 0

    if latest_resume:
        score = latest_resume.ats_score

    return render(
        request,
        'candidate/profile.html',
        {
            'applications': applications,
            'resumes': resumes,
            'score': score
        }
    )