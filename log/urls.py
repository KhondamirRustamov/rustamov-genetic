from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('log', views.log_in, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile/<id>', views.profile, name='profile'),
    path('leaders_list', views.leaders, name='leaders')

]
