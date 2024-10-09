from django.urls import path
from .views import (
    RhSignupView,
    EmployeSignupView,
    CandidatSignupView,
    CustomAuthToken,
    RhOnlyView,
    EmployeOnlyView,
    LogoutView,
)
from .permissions import IsRHUser, IsCandidatUser, IsEmployeUser

urlpatterns = [
    path('signup/rh/', RhSignupView.as_view(), name='signup_rh'),
    path('signup/employe/', EmployeSignupView.as_view(), name='signup_employe'),
    path('signup/candidat/', CandidatSignupView.as_view(), name='signup_candidat'),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('rh/dashboard/', RhOnlyView.as_view(), name='rh-dashboard'),
    path('employe/dashboard/', EmployeOnlyView.as_view(), name='employe-dashboard'),
    path('candidat/dashboard/', EmployeOnlyView.as_view(), name='candidat-dashboard'),
]




# from django.urls import path
# from .views import RhSignupSerializer, EmployeSignupSerializer, CandidatSignupSerializer

# urlpatterns = [
#     path('signup/rh', RhSignupSerializer.as_view),
#     path('signup/employe', EmployeSignupSerializer.as_view),
#     path('signup/candidat', CandidatSignupSerializer.as_view),

# ]

