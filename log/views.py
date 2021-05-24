from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import Profile
from problems.models import Theme, Problem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def signup(request):
    logino=0
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect('theme-list')
    else:
        form = SignUpForm()
    if request.user.is_authenticated:
        logino=123
    else:
        logino=logino
    return render(request, 'log/user.html', {'form': form, 'logino': logino})


def log_in(request):
    logino=0
    if request.user.is_authenticated:
        logino=123
    else:
        logino=logino
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('theme-list')
        else:
            # Return an 'invalid login' error message.
            ...
    else:
        return render(request, 'log/login.html', {'logino': logino})


def profile(request, id):
    logino=0
    if request.user.is_authenticated:
        logino=123
        pro = Profile.objects.get(user=id)
        position = Profile.objects.filter(rate__gt=pro.rate).count()+1
        prob = Problem.objects.all()
        user_solver = str(request.user.id)
        all_problems = [x.theme for x in prob]
        solved = [x.theme for x in prob if user_solver in x.user_solver.split(',')]
        solved_unique = list(dict.fromkeys(solved))
        new=[]
        for y in solved_unique:
            y = [y, len([x for x in solved if x == y]), len([x for x in all_problems if x == y])]
            y.append(int(y[1]/y[2]*100))
            new.append(y)
        context = {'obj': pro,
                    'logino': logino,
                   'position': position,
                   'solved': solved,
                   'new': new
                   }
        return render(request, 'log/Profile.html', context)
    else:
        return redirect('login')


def logout_view(request):
    logino=0
    if request.user.is_authenticated:
        logino=123
        if request.method == 'POST':
            logout(request)
            return redirect('home')
        else:
            return render(request, 'log/logout.html', {'logino': logino})
    else:
        return redirect('home')


def leaders(request):
    logino = 0
    position = Profile.objects.all().order_by('-rate')
    if request.user.is_authenticated:
        logino = 123
        data = {'logino': logino,
                'leaders': position}
        return render(request, 'log/leaders.html', data)
    else:
        data = {'logino': logino,
                'leaders': position}
        return render(request, 'log/leaders.html', data)