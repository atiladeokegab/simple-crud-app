from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    form = ApplicationForm()  # Define form for GET request
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']

            # Save form data to the database
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            # Sending email to the user
            #message_body = f'Thank you! Your form has been submitted, \n{first_name} {last_name}'
            #email_message = EmailMessage("Thanks for the application", message_body, to=[email])
            #email_message.send()
            messages.success(request, "Form submitted successfully!")  # Optional: Display success message
            print(first_name)

    return render(request, 'index.html', {'form': form})

def about(request):
    return render(request, 'about.html')