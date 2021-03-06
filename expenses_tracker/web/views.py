from django.shortcuts import render, redirect
from expenses_tracker.web.forms import CreateProfileForm, CreateExpenseForm, EditExpenseForm, DeleteExpenseForm, \
    EditProfileForm, DeleteProfileForm
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
    profile = get_profile()
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    profile = get_profile()
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show home')

    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
        'profile': profile,
    }

    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    profile = get_profile()
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show home')

    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
        'profile': profile,
    }

    return render(request, 'expense-delete.html', context)


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
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile page')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile-delete.html', context)


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
