from django.shortcuts import render
from django.http import HttpResponse
from CandidateFinder.models import Skill, Job, Candidate


def dashboard(request):
    candidates = Candidate.objects.all().order_by('skills')
    jobs = Job.objects.all()
    total_candidates = candidates.count
    total_software = candidates.filter(skills__name__in=['C++', 'SQL']).count()
    total_backend = candidates.filter(skills__name__in=['NodeJS', 'django']).count()
    total_frontend = candidates.filter(skills__name__in=['VueJS', 'React']).count()

    context = {'candidates':candidates, 'jobs':jobs, 'total_candidates':total_candidates,
    'total_software':total_software,'total_backend':total_backend,
    'total_frontend':total_frontend}

    return render(request, 'dashboard.html', context)


def index(request):
    candidate_list = Candidate.objects.all()
    jobs_list = Job.objects.filter(job_title__exact='Back-end')
    context = {
    "candidate_list" : candidate_list ,
    "jobs_list" : jobs_list
    }

    return render(request, 'index.html', context)
