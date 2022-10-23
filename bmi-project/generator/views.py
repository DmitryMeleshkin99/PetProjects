from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    return render(request, "generator/index.html")

def bmi_result(request):

    sex = request.GET.get('sex')

    growth = int(request.GET.get('growth'))

    weight = int(request.GET.get('weight'))

    bmi = round((weight/growth**2)*10000)

    answer = ''

    if bmi <= 16.49:
        answer = 'Выраженный дефицит массы'
    elif 16.5 < bmi < 18.49:
        answer = 'Дефицит массы тела'
    elif 18.5 < bmi < 24.99:
        answer = 'Нормальная масса тела'
    elif 25 < bmi < 29.99:
        answer = 'Избыточная масса тела'
    elif 30 < bmi < 34.99:
        answer = 'Ожирение первой степени'
    elif 35 < bmi < 39.99:
        answer = 'Ожирение второй степени'
    elif 40 < bmi :
        answer = 'Ожирение третьей степени'


    return render(request, "generator/results.html", {'bmi':bmi,
                                                      'answer':answer,
                                                      'growth':growth,
                                                      'sex':sex,
                                                      'weight':weight })
     


