from django.shortcuts import render
from django.http import HttpResponse
from CandidateFinder.models import Skill, Job, Candidate


def index(request):
    skill_list = Skill.objects.all()
    context = {
    "skill_list" : skill_list
    }

    return render(request, 'index.html', context)
