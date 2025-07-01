from django.shortcuts import render
from django.http import HttpResponse
from tasks_handler.models import Tasks
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        initDate = datetime.strptime(request.POST.get('start-date'), '%Y-%m-%d')
        endDate = datetime.strptime(request.POST.get('end-date'), '%Y-%m-%d')
        print(initDate)
        print(endDate)
        return HttpResponse(
            Tasks.objects.filter(date__gte=datetime.date(initDate)).filter(date__lte=datetime.date(endDate)).values()
        )
    if request.method == 'GET':
        return render(request, 'generateStatus.html')