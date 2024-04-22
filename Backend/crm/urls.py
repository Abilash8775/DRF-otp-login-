from django.urls import path
from . import views
urlpatterns=[
    path("signup/",views.signup_list,name="signup"),
    path("signin/",views.signin_list,name="signin"),
    path("verify/",views.verify_otp,name="verify"),
]