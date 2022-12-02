from django.urls import path
from pybo import views

app_name = 'pybo'
urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail)
]
