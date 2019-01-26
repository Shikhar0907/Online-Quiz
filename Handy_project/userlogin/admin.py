from django.contrib import admin
from .models import User_Signup,quiz_questions,User_results
# Register your models here.
admin.site.register(User_Signup)
admin.site.register(quiz_questions)
admin.site.register(User_results)