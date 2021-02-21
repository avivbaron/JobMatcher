from django.db import models


class Skill(models.Model):

    JAVA_SKILL = 'Java'
    C_SKILL = 'C'
    CPP_SKILL = 'C++'
    SQL_SKILL = 'SQL'
    NODEJS_SKILL = 'NodeJS'
    DJANGO_SKILL = 'django'
    VUEJS_SKILL = 'VueJS'
    REACT_SKILL = 'React'


    CHOICES_SKILL = (
        (JAVA_SKILL, 'Java'),
        (C_SKILL, 'C'),
        (CPP_SKILL, 'C++'),
        (SQL_SKILL, 'SQL'),
        (NODEJS_SKILL, 'NodeJS'),
        (DJANGO_SKILL, 'django'),
        (VUEJS_SKILL, 'VueJS'),
        (REACT_SKILL, 'React'),
    )

    name = models.CharField(max_length=50, choices = CHOICES_SKILL, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):

    SOFTWARE_DEVELOPER = 'Software Developer'
    BACKEND_DEVELOPER = 'Back-end Developer'
    FRONTEND_DEVELOPER = 'Front-end Developer'

    CHOICES_JOB = (
        (SOFTWARE_DEVELOPER, 'Software Developer'),
        (BACKEND_DEVELOPER, 'Back-end Developer'),
        (FRONTEND_DEVELOPER, 'Front-end Developer'),
    )

    job_title = models.CharField(max_length = 50, choices = CHOICES_JOB, default = SOFTWARE_DEVELOPER)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.job_title



class Candidate(models.Model):
    name = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)

    skills = models.ManyToManyField(Skill)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title
