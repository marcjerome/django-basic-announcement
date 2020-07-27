from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AnnouncementForm

@login_required
def home(request):
    form = AnnouncementForm()
    return render(request, 'home.html', {'form': form})

@login_required
def add_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')