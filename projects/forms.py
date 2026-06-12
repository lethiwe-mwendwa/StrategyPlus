from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import TextInput

from accounts.models import Organisation

from .models import Project


class createProjectForm(forms.ModelForm):

    organisation = forms.ModelChoiceField(
        queryset=Organisation.objects.none()
    )

    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )


    class Meta:
        model = Project
        fields = [
            'organisation',
            'name',
            'description',
            'start_date',
            'end_date',
            'budget',
            'status'
        ]