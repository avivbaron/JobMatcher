from django.shortcuts import render
from django.http import HttpResponse
from CandidateFinder.models import Skill, Job, Candidate


def index(request):
    candidate_list = Candidate.objects.all()
    jobs_list = Job.objects.filter(job_title__exact='Back-end')
    context = {
    "candidate_list" : candidate_list ,
    "jobs_list" : jobs_list
    }

    return render(request, 'index.html', context)
