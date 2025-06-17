from django.http import HttpResponse


from django.shortcuts import render

def asd(request):
    return render(request, 'asd.html')