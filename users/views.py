from django.shortcuts import render, redirect
from .forms import UserRegisterForm

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
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
        context = {
            'form': form
        }
    return render(request, 'users/register.html', context)
