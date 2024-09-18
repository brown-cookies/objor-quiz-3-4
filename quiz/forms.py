from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}), required=True, help_text="Enter your username.")
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'id': 'password_field', "class": "form-control form-control-lg"}),
        help_text="Enter a strong password."
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'id': 'confirm_password_field', "class": "form-control form-control-lg"}),
        help_text="Enter the same password again for confirmation."
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}), required=True, help_text="Enter a valid email address.")
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "form-check-input"}), required=False, label="Is Active", initial=False)
    staff = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "form-check-input"}), required=False, label="Is Staff", initial=False)
    admin = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "form-check-input"}), required=False, label="Is Admin", initial=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff', 'is_superuser']
        labels = {
            'is_active': 'Active',
            'is_staff': 'Staff',
            'is_superuser': 'Admin',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("The two password fields must match.")
    
    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
