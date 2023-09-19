from django import forms
from first_app.models import StudentModel


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentModel
        # fields = ["name", "roll", "fathers_name"]
        # exclude = ["address"]
        fields = "__all__"

        labels = {
            "name": "Enter Your Name",
            "roll": "Enter Your Roll",
            "fathers_name": "Enter Your Father's Name"
        }
        widgets = {
            "name": forms.TextInput()
        }
        help_texts = {
            "name": "Write your full name",
        }

        error_messages = {
            "name": {"required": "Your name is required"},
        }
