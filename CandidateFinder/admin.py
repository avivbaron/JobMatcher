from django.contrib import admin

from .models import Job, Skill, Candidate

admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(Candidate)
