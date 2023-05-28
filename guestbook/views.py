from django.shortcuts import render
from .models import Balloon
from django.shortcuts import render, redirect
from .forms import BalloonForm

def balloon_list(request):
    if request.method == 'POST':
        body = request.POST.get('body')
        if body:
            Balloon.objects.create(body=body)
        return redirect('home')  # 방명록 작성 후 리다이렉트

    guestbook_entries = Balloon.objects.all().order_by('-id')
    return render(request, 'home.html', {'guestbook_entries': guestbook_entries})
