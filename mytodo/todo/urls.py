from django.urls import path

from todo import views

app_name = 'todo'
urlpatterns = [
    path('todo/', views.TodosAPIView.as_view()),
    path('todo/<int:pk>/', views.TodoAPIView.as_view()),
    path('done/', views.DoneTodosView.as_view()),
    path('done/<int:pk>/', views.DoneTodoView.as_view()),
]