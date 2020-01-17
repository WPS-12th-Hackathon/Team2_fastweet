from django.contrib.auth import get_user_model, login, authenticate
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

# Create your views here.

User = get_user_model()


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print('hello~~~~~', user)
        if user:
            login(request, user)
            return redirect('threads:thread-list')

    return render(request, 'members/sign_in.html')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        print(username, password, email)

        user, created = User.objects.get_or_create(
            name=username,
            username=username,
            password=password,
            email=email,
        )

        if not created:
            error_msg = ValidationError('같은 아이디, 비밀번호 존재합니다.')
            context = {
                'error': list(error_msg).pop(),
            }
            return render(request, 'members/sign_up.html', context)

        login(request, user)
        return redirect('threads:thread-list')

    return render(request, 'members/sign_up.html')


def log_out(request):
    pass

    # def profile(request, name=None):
    #     curruent_user = request.user
    #     thread_author = name
    #     if name:
    #         if curruent_user == thread_author:
    #             context = {
    #                 'same_user': True
    #             }
    #         else:
    #             context = {
    #                 'same_user': False
    #             }
    #     curruent_user.filter(following__name=thread_author)

    def profile(request, name=None):
        curruent_user = request.user
        thread_author = name
        if name:
            if curruent_user == thread_author:
                context = {
                    'same_user': True
                }
            else:
                context = {
                    'same_user': False
                }
        curruent_user.filter(following__name=thread_author)

    context = {
        'user': request.user,
    }
    return render(request, 'threads/profile.html', context)
