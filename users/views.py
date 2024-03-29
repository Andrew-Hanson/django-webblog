from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from django.contrib import messages
#   message.debug
#   message.info
#   message.success
#   message.warning
#   message.error


# Create your views here.
def register(request):
    if request.method == 'POST':
        # post requests fill out the form with the data that was sent with the request
        # incomplete forms will keep the data that was entered
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()  # saves the user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
        context = {
            'form': form
        }
    return render(request, 'users/register.html', context)


# a wrapper that requires the user to be logged in to access the view
@login_required
def logout_view(request):
    if request.method == 'POST':
        return auth_views.LogoutView.as_view(template_name='users/logout.html')(request)
    # else:
    return redirect('blog-home')


@login_required
def profile(request):
    return render(request, 'users/profile.html')
