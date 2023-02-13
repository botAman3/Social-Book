from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name = "index"),
    path('signUp/' , views.signUp , name="signup"),
    path('signin/' , views.signIn , name="signin"),
    path('logout/' , views.logout , name="logout")
]
