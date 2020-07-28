from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AnnouncementForm
from .models import Announcement

@login_required
def home(request):
    form = AnnouncementForm()
    annoucements = Announcement.objects.all()
    context = {
        'form': form,
        'announcements': annoucements,
    }
    return render(request, 'home.html', context)

@login_required
def add_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('home')

@login_required
def delete_announcement(request, pk):
    try:
        announcement = Announcement.objects.get(id=pk)
        announcement.delete()
    except Announcement.DoesNotExist:
        pass
    return redirect('home')