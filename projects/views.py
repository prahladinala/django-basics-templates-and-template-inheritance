from django.shortcuts import render

from django.http import HttpResponse

def projects(request):
    # return HttpResponse('Here are our projects')
    return render(request, 'projects.html')

def project(request, pk):
    # return HttpResponse('Single Project' + ' ' + str(pk))
    return render(request, 'single-project.html')