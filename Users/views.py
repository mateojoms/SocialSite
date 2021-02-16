from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistration

def register(request):
     if request.method == 'POST':
          form = UserRegistration(request.POST)
          if form.is_valid():
              form.save()
              username = form.cleaned_data.get('username')
              messages.success(request,f'Your account has been successfully created!You can now login')
              return redirect('login')
     else:
         form = UserRegistration()
     return render(request,'Users/register.html',{'form':form})
@login_required
def profile(request):
    return render(request,'Users/profile.html')
