from django.contrib.auth import get_user_model, login, authenticate, logout
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

        if User.objects.filter(username=username).exists():
            error_msg = ValidationError('같은 아이디, 비밀번호 존재합니다.')
            context = {
                'error': list(error_msg).pop(),
            }
            return render(request, 'members/sign_up.html', context)

        user = User.objects.create_user(
            name=username,
            username=username,
            password=password,
            email=email,
        )

        login(request, user)
        return redirect('threads:thread-list')

    return render(request, 'members/sign_up.html')


def log_out(request):
    logout(request)
    return redirect('members:sign-in')

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
    #     curruent_user.filter(following__namo=thread_author)


def profile(request, thread_name=None):
    if thread_name:
        print(thread_name, type(thread_name))
        current_user = request.user
        profile_user = User.objects.get(username=thread_name)
        print('현유저는 : ', request.user)
        print('프로필유저는 : ', profile_user)
        print(request.user == profile_user)

        context = dict()
        if current_user == profile_user:
            context['same_user'] = True

        if current_user.following.filter(username=profile_user):
            context['following'] = True

        return render(request, 'threads/profile.html', context)

    context = {
        'user_name': request.user.username,
        'following_count': request.user.following.all().count(),
        'follower_count': request.user.counterpart_relation_set.all().count(),
    }

    print(context['following_count'])
    return render(request, 'threads/profile.html', context)
