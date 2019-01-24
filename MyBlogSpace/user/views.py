from django.shortcuts import render,redirect
from django.contrib import messages
from .form import userRegistrationForm

def registration(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            print('hi')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account is created for {username}')
            return redirect('blog-home')
    else:
        form = userRegistrationForm()
    
    return render(request,'user/register.html', {'form': form})


