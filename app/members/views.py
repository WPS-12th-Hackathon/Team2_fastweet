from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect

# Create your views here.

User = get_user_model()


def sign_in(request):
    return render(request, 'members/sign_in.html')


def sign_up(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(
            name=username,
            password=password,
            email=email,
        )
        login(request, user)
        return redirect('')


def log_out(request):
    pass

def profile(request):
    pass