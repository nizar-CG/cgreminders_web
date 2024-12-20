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


# Form for EmailGroups
class EmailGroupForm(forms.ModelForm):
    class Meta:
        model = EmailGroups
        fields = ['group_name']  # Fields to display in the form

# Form for EmailGroupDetails
class EmailGroupDetailForm(forms.ModelForm):
    class Meta:
        model = EmailGroupDetails
        fields = ['email']# Only show the email field in the form
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control", 'type': 'email'}),
        }

    def __init__(self, *args, **kwargs):
        # Pop the 'group' argument passed from the view
        self.group = kwargs.pop('group', None)
        super().__init__(*args, **kwargs)


        if self.group:
            self.fields['group_detail'] = forms.ModelChoiceField(
                queryset=EmailGroups.objects.filter(id=self.group.id),
                widget=forms.HiddenInput(),
                initial=self.group
            )




# Formulaire pour Tasks
class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ['user', 'state']
        due_date = forms.DateField(
        label="Due Date",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )
        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "main_object": forms.TextInput(attrs={"class": "form-control"}),
            "remaindertype": forms.Select(attrs={"class": "form-control"}),
            "mailgroup": forms.Select(attrs={"class": "form-control"}),
            "state": forms.Select(attrs={"class": "form-control"}),
            'due_date': forms.DateInput(format="%Y-%m-%d", attrs={"type": "date", "class": "form-control"}),

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
