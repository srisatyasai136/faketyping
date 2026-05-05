from django.urls import path
from . import views
urlpatterns=[
    path("",views.login,name="login"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('start_work/', views.start_work, name='start_work'),
path('submit_work/', views.submit_work, name='submit_work'),
    path('logout/', views.logout, name='logout')
]