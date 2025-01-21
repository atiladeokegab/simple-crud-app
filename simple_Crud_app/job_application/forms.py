from django import forms
class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField(max_length=80)
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # Optional: Use HTML5 date input
    )
    occupation = forms.CharField(max_length=80)