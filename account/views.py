from django.shortcuts import render
from .forms import RegisterUser
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'userRegistation/home.html')


def signUp(request):
    try:
        user_form = RegisterUser(request.POST or None)
        if user_form.is_valid():
            user_form.save()
            user_form = RegisterUser()
            messages.success(request, "USER CREATED SUCCESSFULLY...")
    except ValueError:
        user_form = RegisterUser()

    context = {'user_form': user_form}
    return render(request, 'userRegistation/signUp.html', context)


def createUser(request):
    form = RegisterUser()
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'userRegistation/login.html', context)


