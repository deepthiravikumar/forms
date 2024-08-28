from django.urls import path
from . import views

urlpatterns=[
    path('app/', views.user_profile_view, name='user_profile_view'),
    path('submit-profile/', views.submit_profile, name='submit_profile'),

]