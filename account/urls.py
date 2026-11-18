from django.urls import path
from account.views import Register, Login, VerifyCode

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('verify-otp/', VerifyCode.as_view())
]
