
from django.shortcuts import render, redirect
from .models import DB
from .forms import DBForm

def main(request):
    return render(request, 'app/main.html',{
        'db':DB.objects.all()
    })

def show(request, idd):
    return render(request, 'app/show.html', {
    'db':DB.objects.get(pk=idd),
    })

def edit(request, idd):
    return render(request, 'app/edit.html', {
    'db':DB.objects.get(pk=idd),
    'dbform':DBForm(instance=DB.objects.get(pk=idd)),
    })

def update(request, idd):
    if request.method == "POST":
        if DBForm(request.POST, instance=DB.objects.get(pk=idd)).is_valid():
            DBForm(request.POST, instance=DB.objects.get(pk=idd)).save()
        return redirect('appname:show', idd)

def delete(request, idd):
    if request.method:
        DB.objects.get(pk=idd).delete()
    return redirect('main')


def new(request):
    return render(request, 'app/new.html',{
    'dbform':DBForm(),
    })

def create(request):
    if request.method == "POST":
        if DBForm(request.POST).is_valid():
            DBForm(request.POST).save()
        return redirect('main')

def test(request):
    return render(request, 'app/test.html')
