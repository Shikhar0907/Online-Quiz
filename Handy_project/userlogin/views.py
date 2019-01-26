from collections import defaultdict
import pandas as pd
from django.shortcuts import render
from .forms import userdetails,questions
from .models import quiz_questions, User_results
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializer import QuestionSerializer

# Create your views here.

name = ""
category = ""

def indexpage(request):
    return(render(request,'index.html'))

def quiz(request,name):
    question = quiz_questions.objects.filter(category=category)
    print(question)
    return render(request,'Quiz.html',{'name':name,'question': question})

def answers(request):
    global category
    score = 0
    question = quiz_questions.objects.filter(category=category)


    global name
    correct_answers = []
    quiz_ques = []
    user_ans = []
    for ques in question:
        correct = ques.answers
        entered_answer = request.POST.get(str(ques.id))
        quiz_ques.append(ques.questions)
        correct_answers.append(correct)
        user_ans.append(entered_answer.strip())
        print(correct,entered_answer)
        if correct == entered_answer.strip():
            score = score + 1

    print(user_ans)
    print(correct_answers)
    for i in range(len(quiz_ques)):
        User_results.objects.create(User_name=name,question=quiz_ques[i],answer=correct_answers[i],user_answer=user_ans[i])

    result = {'score': score}
    return render(request,'result.html',result)

def loginpage(request):
    global name
    global category
    form = userdetails()

    if request.method == "POST":
        form = userdetails(request.POST)

        if form.is_valid():
            request.session['services'] = form.cleaned_data['services']
            form.save(commit=True)
            name = form.cleaned_data['name']
            category = form.cleaned_data['services']
            return quiz(request,name)

        else:
            print("Please enter the full form")

    return render(request,'form.html',{'form':form})

def resultpage(request):

    res = User_results.objects.all()


    User_questions_hashmap = defaultdict(lambda :defaultdict(list))
    i = 0
    for data in res:
        User_questions_hashmap[data.User_name][i].append(data)
        i += 1

    for obj in User_questions_hashmap:
        User_questions_hashmap[obj].default_factory = None

    print(User_questions_hashmap)
    return render(request,'user_results.html',{'res':res,'hashmap':dict(User_questions_hashmap)})

def question_view(request):
    ques = quiz_questions.objects.all()
    return render(request,'question_view.html',{'questions':ques})



def leaders(request):
    res = User_results.objects.all()
    leader = defaultdict(list)
    final = defaultdict(lambda :defaultdict(list))
    for res in res:
        print(res.answer)
        print(res.User_name,res.user_answer)
        if str(res.answer) == str(res.user_answer):
            leader[res.User_name].append(1)
        else:
            leader[res.User_name].append(0)

    for key,value in leader.items():
        leader[key] = sum(value)
    new_dict = pd.DataFrame([leader])
    new_dict = new_dict.T.set_axis(['Score'], axis=1, inplace=False).rename_axis('Name',axis=0).reset_index()
    new_dict['Rank'] = new_dict.Score.rank(pct=True)
    new_dict = new_dict.sort_values(['Rank','Name'],ascending=[0,1])

    return render(request,'leaders.html',{'dict':new_dict})


class QuesListSearchAPIView(APIView):

    def get(self,request,format=None):
        obj = quiz_questions.objects.all()
        serializer = QuestionSerializer(obj,many=True)
        return Response(serializer.data)


class QuesCreateAPIView(generics.CreateAPIView):
    obj = quiz_questions.objects.all()
    serializer_class = QuestionSerializer

class QuesDetailAPIView(generics.RetrieveAPIView):
    queryset = quiz_questions.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'

    def get_queryset(self,*args,**kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id')
        return(quiz_questions.objects.get(id = kw_id))

class QuesUpdateAPIView(generics.UpdateAPIView):
    queryset = quiz_questions.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'


class QuesDeleteAPIView(generics.DestroyAPIView):
    queryset = quiz_questions.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'
