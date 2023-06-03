from django.shortcuts import render
from .models import Balloon
from django.shortcuts import render, redirect
from .forms import BalloonForm
from django.views.decorators.csrf import csrf_exempt


def balloon_list(request):
    if request.method == 'POST':
        form = BalloonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BalloonForm()
    
    guestbook_entries = Balloon.objects.all().order_by('-id')
    return render(request, 'home.html', {'guestbook_entries': guestbook_entries, 'form': form})

