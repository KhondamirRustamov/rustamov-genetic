from django.shortcuts import render, redirect

from django.views.generic import DetailView, ListView

from .models import Theme, Problem
from log.models import Profile

# Create your views here.


def ThemeListView(request):
    themes = Theme.objects.all()
    pro = Problem.objects.all()
    number = pro.count()
    solved = 0
    user_solver = 0
    logino = 0
    if request.user.is_authenticated:
        logino=123
        user_solver = str(request.user.id)
        solved = len([x for x in pro if user_solver in x.user_solver.split(',')])
    data = {'themes': themes,
            'usero': user_solver,
            'number': number,
            'solved': solved,
            'progress': int(solved / number * 100),
            'logino': logino}
    return render(request, 'problems/theme_list.html', data)


def ThemeDetailView(request, id):
    theme = Theme.objects.get(id=id)
    pro = Problem.objects.filter(theme=theme)
    number = pro.count()
    solved = 0
    user_solver=0
    logino=0
    if request.user.is_authenticated:
        logino=123
        user_solver = str(request.user.id)
        solved = len([x for x in pro if user_solver in x.user_solver.split(',')])
    data = {'problems': pro,
            'usero': user_solver,
            'number': number,
            'solved': solved,
            'progress': int(solved/number*100),
            'logino': logino,
            'theme': theme}
    return render(request, 'problems/problem_list.html', data)


def ProblemDetailView(request, id):
    problem = Problem.objects.get(id=id)
    theme = Theme.objects.get(name=problem.theme)
    text = ''
    error = ''
    logino=0
    data = {'problem': problem,
            "text": text,
            'error': error,
            'logino': logino,
            'theme': theme}

    if request.user.is_authenticated:
        logino=123
        if str(request.user.id) not in problem.user_solver:
            if request.method == "POST":
                answer = request.POST['answer']
                if answer == problem.answer:
                    pro = Profile.objects.get(user=request.user.id)
                    rate = pro.rate + problem.ball
                    pro.rate = rate
                    pro.save()
                    user_solver = problem.user_solver + ',' + str(request.user.id)
                    problem.user_solver = user_solver
                    problem.save()
                    text = "Вы решили задачу правильно. Ваш рейтинг = %s XP" % rate
                    data = {'problem': problem,
                            "text": text,
                            'error': error,
                            'logino': logino,
                            'theme': theme
                            }
                    return render(request, 'problems/problem.html', data)
                else:
                    text = "Ответ неверен"
                    data = {'problem': problem,
                            "text": text,
                            'error': error,
                            'logino': logino,
                            'theme': theme
                            }
                    return render(request, 'problems/problem.html', data)

            else:
                data = {'problem': problem,
                        "text": text,
                        'error': error,
                        'logino': logino,
                        'theme': theme
                        }
                return render(request, 'problems/problem.html', data)
        else:
            error = "Задача решена"
            data = {'problem': problem,
                    "text": text,
                    'error': error,
                    'logino': logino,
                    'theme': theme
                    }
            return render(request, 'problems/problem.html', data)
    else:
        return redirect('login')