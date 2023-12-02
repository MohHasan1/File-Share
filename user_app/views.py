from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import logout
from .forms import UserRegisterForm


def registration(request):
    if request.method == "POST":
        regForm = UserRegisterForm(request.POST)

        if regForm.is_valid():
            regForm.save()

            # Logout the user after successful registration (will be redirect to home but to access home u need to login!)
            logout(request)
    
            target_url = reverse('sharing_app:home')
            return redirect(target_url)
        
    else:
        # To load the blank with prev inputs.
        regForm = UserRegisterForm()

    return render(request, 'user/signupMub.html', {'regForm': regForm})

@login_required
def profile(request):
    #return render(request, 'user/profile.html', {})
    return render(request, 'share/profilePageMub.html', {})