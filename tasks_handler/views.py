from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Tasks
from utils.standard_responses import error_response, success_response

def index(request):
    return render(request, template_name='index.html')

def tasks(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        jira = request.POST.get('jira_id')
        goal = request.POST.get('goal')
        status = request.POST.get('status')
        steps = request.POST.get('steps')
        links = request.POST.getlist('links[]')
        next_steps = request.POST.get('next_steps')
        if not title:
            return error_response(error_code=401, message='Title is a required field')
        try:
            task = Tasks(
                title=title,
                jira_id=jira,
                objective=goal,
                current_status=status,
                steps_taken=steps,
                relevant_links=links,
                next_steps=next_steps
            )
            task.save()
            return redirect('/tasks')
        except Exception as e:
            print(f'EXCEPTION: {e} occured while creating task')
            return error_response(error_code=500, message='Failed to create task')
    if request.method == 'GET':
        # try:
        all_tasks = Tasks.objects.all().values()
        result = {}
        result['status_code'] = 201
        result['message'] = 'Data retrieved'
        result['data'] = all_tasks
        return render(request, 'tasks.html', result)
        
    return HttpResponse('invalid request')

def task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    return render(request, 'task_detail.html', {'task': task})