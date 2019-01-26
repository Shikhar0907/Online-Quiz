from django.db import models

# Create your models here.

class User_Signup(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True,max_length=50)
    services = models.CharField(max_length=20)

    def __str__(self):
        return(self.name)

class quiz_questions(models.Model):
    category = models.CharField(max_length=30)
    questions = models.CharField(max_length=100)
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    answers = models.CharField(max_length=200)

    def __str__(self):
        return(self.category)


class User_results(models.Model):
    User_name = models.CharField(max_length=30)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)
    user_answer = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(self.User_name)




