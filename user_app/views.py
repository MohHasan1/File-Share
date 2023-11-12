from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import UserRegisterForm

def registration(request):
    if request.method == "POST":
        regForm = UserRegisterForm(request.POST)

        if regForm.is_valid():
            regForm.save()
    
            target_url = reverse('sharing_app:home')
            return redirect(target_url)
        
        else:
            pass
    else:
        # To load the blank with prev inputs.
        regForm = UserRegisterForm()

    return render(request, 'user/register.html', {'regForm': regForm})

@login_required
def profile(request):
    return render(request, 'user/profile.html', {})