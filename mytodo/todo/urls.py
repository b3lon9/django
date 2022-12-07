from django.urls import path

from todo import views

app_name = 'todo'
urlpatterns = [
    path('todo/', views.TodosAPIView.as_view()),
]
