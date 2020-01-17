from django.urls import path

from members.views import sign_up, sign_in, log_out, profile

app_name = 'members'

urlpatterns = [
    path('', sign_in, name='sign-in'),
    path('signup/', sign_up, name='sign-up'),
    path('logout/', log_out, name='log-out'),
    path('profile/', profile, name='profile'),
    path('profile/<int:pk>', profile, name='profile'),
]
