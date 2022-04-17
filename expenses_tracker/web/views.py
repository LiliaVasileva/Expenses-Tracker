from django.shortcuts import render, redirect

from expenses_tracker.web.forms import CreateProfileForm
from expenses_tracker.web.models import Profile


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    context ={
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    pass

def edit_expense(request):
    pass

def delete_expense(request):
    pass

def show_profile(request):
    pass

def profile_edit(request):
    pass

def delete_profile(request):
    pass


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)

