from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 질문(Question)
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 제목
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

# 답변(Answer)
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
