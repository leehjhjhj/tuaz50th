from django.shortcuts import render
from .models import Balloon
from django.shortcuts import render, redirect
from .forms import BalloonForm

def balloon_list(request):
    balloons = Balloon.objects.all()
    return render(request, 'home.html', {'balloons': balloons})

def create_balloon(request):
    if request.method == 'POST':
        form = BalloonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('balloon_list')  # 말풍선 작성 후 말풍선 목록 페이지로 리다이렉트
    else:
        form = BalloonForm()
    return render(request, 'create_balloon.html', {'form': form})

def home(request):
    return render(request, 'home.html')