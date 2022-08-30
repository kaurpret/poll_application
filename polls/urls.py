from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('email',views.email,name="email"),
    path('sign',views.sign,name="sign"),
    path('login',views.login,name="login"),
    path('logout_user',views.logout_user,name="logout_user"),
    path('dash',views.dash,name="dash"),
    path('change',views.change,name='change'),
    path('change_pass',views.change_pass,name='change_pass')
]