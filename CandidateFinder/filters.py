import django_filters
from django import forms
from .models import *

SOFTWARE_DEVELOPER = 'Software Developer'
BACKEND_DEVELOPER = 'Back-end Developer'
FRONTEND_DEVELOPER = 'Front-end Developer'

CHOICES_JOB = (
    (SOFTWARE_DEVELOPER, 'Software Developer'),
    (BACKEND_DEVELOPER, 'Back-end Developer'),
    (FRONTEND_DEVELOPER, 'Front-end Developer'),
)

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


class CandidateFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains')
    skills = django_filters.MultipleChoiceFilter(field_name='skills', choices=CHOICES_SKILL, widget=forms.CheckboxSelectMultiple)
    job = django_filters.MultipleChoiceFilter(field_name='jobs', choices=CHOICES_JOB, widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = Candidate
        fields = '__all__'
        exclude = ['name', 'email', 'phone']
