from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import userRegistrationForm

def registration(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            print('hi')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created.')
            return redirect('login')
    else:
        form = userRegistrationForm()
    return render(request,'user/register.html', {'form': form})

@login_required
def profile(request):
    return render(request,'user/profile.html')



