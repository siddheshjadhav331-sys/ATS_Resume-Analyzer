from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ResumeForm
from .models import Resume
from .skill_extractor import extract_skills

@login_required
def upload_resume(request):

    if request.method == 'POST':

        form = ResumeForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            resume = form.save(commit=False)

            resume.candidate = request.user

            resume.save()

            return redirect(
                'candidate_dashboard'
            )

    else:

        form = ResumeForm()

    return render(
        request,
        'candidate/upload_resume.html',
        {
            'form': form
        }
    )


@login_required
def analysis_view(request):

    resume = Resume.objects.filter(
        candidate=request.user
    ).last()

    skills = []

    if resume:

        skills = extract_skills(
            resume.resume_file.path
        )

    required_skills = [
        'Python',
        'Django',
        'SQL',
        'Docker',
        'Machine Learning'
    ]

    missing_skills = []

    for skill in required_skills:

        if skill not in skills:

            missing_skills.append(skill)

    matched_skills = len(
        required_skills
    ) - len(
        missing_skills
    )

    score = int(
        (
            matched_skills
            /
            len(required_skills)
        ) * 100
    )

    if resume:

        resume.ats_score = score

        resume.save()

    return render(
        request,
        'candidate/analysis.html',
        {
            'skills': skills,
            'missing_skills': missing_skills,
            'score': score
        }
    )