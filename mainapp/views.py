from django.shortcuts import render, HttpResponseRedirect
from .models import Lesson
from django.http import FileResponse, Http404


def main(request):
    return render(request, 'mainapp/robot-main.html')


def lk(request):
    if request.user.is_authenticated:
        return render(request, 'mainapp/robot-learn.html')
    else:
        return HttpResponseRedirect('/auth/login/')



def contact(request):
    return render(request, 'mainapp/contacts.html')


def lesson1(request):
    try:
        return FileResponse(open('media/lesson1.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404('not found')


def lesson2(request):
    try:
        return FileResponse(open('media/lesson2.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404('not found')


def lesson3(request):
    try:
        return FileResponse(open('media/lesson3.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404('not found')