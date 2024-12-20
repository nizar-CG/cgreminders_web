from django import forms
from .models import RemainderTypes, EmailGroups, EmailGroupDetails, Tasks, MailLog


# Formulaire pour RemainderTypes
class RemainderTypesForm(forms.ModelForm):
    class Meta:
        model = RemainderTypes
        fields = ["label", "before_duration", "remainder_frequency"]
        widgets = {
            "label": forms.TextInput(attrs={"class": "form-control"}),
            "before_duration": forms.NumberInput(attrs={"class": "form-control"}),
            "remainder_frequency": forms.NumberInput(attrs={"class": "form-control"}),
        }


# Formulaire pour EmailGroups
class EmailGroupsForm(forms.ModelForm):
    class Meta:
        model = EmailGroups
        fields = ["group_name"]
        widgets = {
            "group_name": forms.TextInput(attrs={"class": "form-control"}),
        }


# Formulaire pour EmailGroupDetails
class EmailGroupDetailsForm(forms.ModelForm):
    class Meta:
        model = EmailGroupDetails
        fields = ["email", "group_detail"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "group_detail": forms.EmailInput(attrs={"class": "form-control"}),
        }


# Formulaire pour Tasks
class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["description", "remaindertype", "mailgroup", "state"]
        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "remaindertype": forms.Select(attrs={"class": "form-control"}),
            "mailgroup": forms.Select(attrs={"class": "form-control"}),
            "state": forms.Select(attrs={"class": "form-control"}),
        }


# Formulaire pour MailLog
class MailLogForm(forms.ModelForm):
    class Meta:
        model = MailLog
        fields = ["description", "dateofsend", "email_group"]
        widgets = {
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "dateofsend": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "email_group": forms.Select(attrs={"class": "form-control"}),
        }
