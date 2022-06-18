from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def home(request):
    context = {
        'title': "Home",
    }
    return render(request, 'portal/home.html', context)


@login_required
def profile(request):
    context = {
        "title": "Profile",
    }
    return render(request, 'portal/profile.html', context)


@login_required
def payment_method(request):
    context = {
        "title": "Payment Method",
    }
    return render(request, 'portal/payment_method.html', context)
