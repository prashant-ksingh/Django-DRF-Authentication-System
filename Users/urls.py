from django.urls import path
from . import views
from .views import LoginView, RegistrationView, VerificationView, ForgotPasswordView, ResetPasswordView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('verify/', VerificationView.as_view(), name='verify'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
]