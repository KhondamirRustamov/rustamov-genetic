from django.shortcuts import render

# Create your views here.


def index(request):
    logino=0
    if request.user.is_authenticated:
        logino=123
        form = {"user": request.user,
                'logino': logino}
        return render(request, 'main/index.html', form)
    else:
        form = {"user": 0,
                'logino': logino}
        return render(request, 'main/index.html', form)
