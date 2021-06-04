from django.shortcuts import render, redirect

from .forms import RegisterForm


def signup(request):
    """user registration"""

    if request.method == "POST":
        form_signup = RegisterForm(request.POST)
        if form_signup.is_valid():
            form_signup.save()
            return redirect('core:home')
    else:
        form_signup = RegisterForm()

    context = {'form_signup': form_signup,}

    return render(request, 'authentication/signup.html', context)

