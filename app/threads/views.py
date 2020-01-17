# Create your views here.
from django.shortcuts import render, redirect

from threads.models import Thread, ThreadLike


def thread_list(request):
    threads = Thread.objects.all()
    context = {
        'threads': threads
    }
    print(threads)
    return render(request, 'threads/thread-list.html', context)


def thread_like(request, pk):
    thread = Thread.objects.get(pk=pk)
    user = request.user

    thread_like_qs = ThreadLike.objects.filter(thread=thread, user=user)

    if thread_like_qs.exists():
        thread_like_qs.delete()

    else:
        ThreadLike.objects.create(thread=thread, user=user)

    return redirect('threads:thread-list')
