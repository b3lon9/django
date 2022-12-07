from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('profile/<int:pk>/', views.ProfileView.as_view()),
]
