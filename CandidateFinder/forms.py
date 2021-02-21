from django.forms import ModelForm
from .models import Candidate, Job, Skill

class CandidateForm(ModelForm):
	class Meta:
		model = Candidate
		fields = '__all__'
