from django.urls import path
from . import views

urlpatterns = [
    path('', views.ThemeListView, name='theme-list'),
    path('<id>', views.ThemeDetailView, name='theme'),
    path('theme/<id>', views.ProblemDetailView, name='problem')
]