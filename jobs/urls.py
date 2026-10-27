from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'job/<int:job_id>/',
        views.job_detail,
        name='job_detail'
    ),

    path(
        'job/<int:job_id>/apply/',
        views.apply_job,
        name='apply_job'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    # ABOUT
    path(
        'about/',
        views.about,
        name='about'
    ),

    # CONTACT
    path(
        'contact/',
        views.contact,
        name='contact'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),
]