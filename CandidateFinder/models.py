from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Job(models.Model):
    job_title = models.CharField(max_length=50)
    skill = models.ForeignKey('Skill', null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.title



class Candidate(models.Model):
    title = models.CharField(max_length=50, null=True)
    # exp_years = models.PositiveIntegerField()
    skill = models.ForeignKey('Skill', related_name='skill', null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
