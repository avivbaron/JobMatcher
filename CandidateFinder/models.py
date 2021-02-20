from django.db import models

class Skill(models.Model):
    skill_name = models.CharField(max_length=50)

class Job(models.Model):
    job_name = models.CharField(max_length=50)
    skill_id = models.ForeignKey(Skill, on_delete = models.CASCADE)

class Candidate(models.Model):
    candidate_name = models.CharField(max_length=50)
    # exp_years = models.PositiveIntegerField()
    skill_id = models.ForeignKey(Skill, on_delete = models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete = models.CASCADE)
