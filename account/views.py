from django.core.mail import mail_admins
from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserRegistrationForm, CallbackRequestForm


def callback_request(request):
    # Check if user is logged in, if yes, associate phone number with user
    # Save contact details to database
    # Alert the admin of a new callback request.

    if request.method == "POST":
        form = CallbackRequestForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            mail_admins(
                subject="New callback request",
                message=f"The following client has requested a call back\n\n\nName of client: {name}\n\nPhone number "
                        f"of client: {phone}",
                fail_silently=False,
            )
            html_msg = f'<div style="margin-bottom: 20px" class="section-heading"><h2>Thanks <em>{name}</em> we will ' \
                       f'get in touch with you soon!</h2></div> '
            return HttpResponse(html_msg)
        else:
            return HttpResponse(status=400)


def home(request):
    context = {
        'title': "Home",
        'form': CallbackRequestForm,
    }
    return render(request, 'account/home.html', context)


def contact(request):
    context = {
        "title": "Contact",
    }
    return render(request, 'account/contact.html', context)


def services(request):
    context = {
        "title": "Services",
    }
    return render(request, 'account/services.html', context)


def about(request):
    context = {
        "title": "About",
    }
    return render(request, 'account/about.html', context)


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the user object
            new_user.save()

            context = {
                "new_user": new_user,
                "title": "Registration done",
            }
            return render(request, 'account/register_done.html', context)
    else:
        user_form = UserRegistrationForm()
        context = {
            'user_form': user_form,
            "title": "Register"
        }
    return render(request, 'account/register.html', context)
