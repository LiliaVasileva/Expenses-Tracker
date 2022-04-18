from django.shortcuts import render, redirect

from expenses_tracker.web.forms import CreateProfileForm, CreateExpenseForm
from expenses_tracker.web.models import Profile, Expense


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    expenses = Expense.objects.all()
    profile_budget_left = profile.budget - sum(expense.price for expense in expenses)

    context = {
        'profile': profile,
        'expenses': expenses,
        'profile_budget_left': profile_budget_left,
    }

    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request):
    pass


def delete_expense(request):
    pass


def show_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(expense.price for expense in expenses)
    profile_items = len(expenses)
    context = {
        'profile': profile,
        'budget_left': budget_left,
        'profile_items': profile_items,
    }
    return render(request, 'profile.html', context)


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
