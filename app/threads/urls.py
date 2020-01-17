from django.urls import path

from threads.views import thread_list, thread_like

app_name = 'threads'

urlpatterns = [
    # /home/
    path('thread-list/', thread_list, name='thread-list'),
    path('thread-like/<int:pk>', thread_like, name='thread-like')

]