from django import forms
from django.core import validators


class contactForm(forms.Form):
    name = forms.CharField(label="Full Name: ",
                           required=False, widget=forms.Textarea(attrs={"placeholder": "Enter your longest name!"}))
    file = forms.ImageField()
    email = forms.EmailField(
        label="User Email", required=False)
    age = forms.IntegerField(label="Age", initial=1)
    weight = forms.FloatField(label="weight", initial=2)
    balance = forms.DecimalField(label="Balance", initial=3)
    check = forms.BooleanField(label="Are you Happy?", initial=True)
    birthdate = forms.DateField(widget=forms.DateInput(attrs={"type": "Date"}))
    appointment = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "Datetime-local"}))

    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect)

    MEAL = [("Pepperoni", "Pepperoni"),
            ("Mashroom", "Mashroom"), ("Beef", "Beef")]
    pizza = forms.MultipleChoiceField(
        choices=MEAL,  widget=forms.CheckboxSelectMultiple)


""" class studentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data["name"]
        valemail = self.cleaned_data["email"]
        if len(valname) < 10:
            raise forms.ValidationError("Must be at least 10 characters.")
        if ".com" not in valemail:
            raise forms.ValidationError("Your email must contain .com")
 """


class studentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(
        10, message="You crossed max limit of characters 10")])
    email = forms.EmailField(
        validators=[validators.EmailValidator("Plase enter valid email")])
    age = forms.IntegerField(
        validators=[validators.MaxValueValidator(35, "Age shouldn't cross 35"), validators.MinValueValidator(18, "You should be above 18")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(
        allowed_extensions=["pdf"], message="You are allowed to upload only PDF file.")])


class passwordvalidatonproject(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        clean_data = super().clean()
        name = self.cleaned_data["name"]
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if password != confirm_password:
            raise forms.ValidationError(message="Password not matched")
        if len(name) < 10:
            raise forms.ValidationError(
                message="Name must have at least 10 chars.")
