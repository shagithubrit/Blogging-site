from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
def signup_view(request):
    if request.method=='POST':
     #validating user information
     form=UserCreationForm(request.POST)
     if form.is_valid():
      user= form.save()
        #log the user in a
     login(request,user)
     return redirect('articles:list')
    else:
      form=UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form  = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})

def logout_view(request):
  if request.method=='POST':
    logout(request)  # here you don't need to mention which user to logout , django automatically knows that , that you want to log out cureent logged in user
    return redirect('articles:list')
